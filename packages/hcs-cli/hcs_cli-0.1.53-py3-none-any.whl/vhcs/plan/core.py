"""
Copyright 2023-2023 VMware Inc.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import threading
import typing
import inspect
import re
from subprocess import CalledProcessError
from copy import deepcopy
import vhcs.ctxp.data_util as data_util
from . import dag
from . import context
from .helper import PlanException, process_template
from .actions import actions
from .kop import KOP
from importlib import import_module

import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def _prepare_data(data: dict, additional_context: dict, target_resource_name: str):
    if additional_context:
        common_items = data_util.get_common_items(additional_context.keys(), data.keys())
        if common_items:
            raise PlanException("blueprint and context have conflict keys: " + str(common_items))
        data.update(additional_context)
    blueprint, pending = process_template(data)

    if (
        target_resource_name
        and target_resource_name not in blueprint["resources"]
        and target_resource_name not in blueprint["runtimes"]
    ):
        raise PlanException("Target resource or runtime not found: " + target_resource_name)

    for k, v in pending.items():
        if v.startswith("defaults.") or v.startswith("vars."):
            if not k.find(".conditions."):
                raise PlanException(
                    f"Invalid blueprint. Unresolved static references. Variable not found: {v}. Required by {k}"
                )
    deployment_id = blueprint["deploymentId"]
    state_file = deployment_id + ".state.yml"
    prev = data_util.load_data_file(state_file, default={})
    state = {"pending": pending}
    state.update(blueprint)
    if "providers" not in state:
        state["providers"] = {}
    if "runtimes" not in state:
        state["runtimes"] = {}
    state["output"] = prev.get("output", {})
    state["destroy_output"] = prev.get("destroy_output", {})
    state["log"] = prev.get("log", {})
    exec_log = state["log"]
    if "create" not in exec_log:
        exec_log["create"] = []
    if "delete" not in exec_log:
        exec_log["delete"] = []

    context.set("deploymentId", state["deploymentId"])

    # try solving more variables
    # for k, v in state['output'].items():
    #     if not v:
    #         continue
    #     if not _has_successful_deployment(state, k):
    #         continue
    #     _resolve_pending_keys(state, k)

    return blueprint, state, state_file


# def _has_successful_deployment(state, name):
#     for v in state['log']['create']:
#         if v['name'] != name:
#             continue
#         if v['action'] == 'success':
#             return True


def apply(
    data: dict,
    additional_context: dict = None,
    target_resource_name: str = None,
    include_dependencies: bool = True,
    concurrency: int = 4,
):
    blueprint, state, state_file = _prepare_data(data, additional_context, target_resource_name)
    state["log"]["create"] = []  # clear deploy log

    def deploy_resource_or_runtime(name, res_data):
        _deploy_res(name, res_data, state)
        data_util.save_data_file(state, state_file)

    def process_resource_node(name: str):
        if name in blueprint["resources"]:
            res_data = blueprint["resources"][name]
            return deploy_resource_or_runtime(name, res_data)
        elif name in blueprint["runtimes"]:
            res_data = blueprint["runtimes"][name]
            return deploy_resource_or_runtime(name, res_data)
        elif name in blueprint["providers"]:
            # ignore.
            # Provide init is always ensured before running the resource
            # and does not follow deploy/destroy sequenct.
            pass
        else:
            # defaults, vars, etc.
            pass

    try:
        dag.process_blueprint(
            blueprint=blueprint,
            fn_process_node=process_resource_node,
            continue_on_error=False,
            reverse=False,
            concurrency=concurrency,
            target_node_name=target_resource_name,
            include_dependencies=include_dependencies,
        )
    except CalledProcessError as e:
        raise PlanException(str(e))
    finally:
        data_util.save_data_file(state, state_file)


def _parse_statement_for(res_name, state) -> typing.Tuple[str, list]:
    # for: email in vars.userEmails
    res = state["resources"][res_name]
    for_statement = res.get("for")
    if not for_statement:
        return None, None
    pattern = r"(.+?)\s+in\s+(.+)"
    matcher = re.search(pattern, for_statement)

    def _raise_error(reason):
        raise PlanException(f"Invalid for statement: {reason}. Resource={res_name}, statement={for_statement}")

    if not matcher:
        _raise_error("Invalid syntax")
    var_name = matcher.group(1)
    values_name = matcher.group(2)
    values = _get_value_by_path(state, values_name, f"resources.{res_name}.for")
    if not isinstance(values, list):
        reason = "The referencing value is not a list. Actual type=" + type(values).__name__
        _raise_error(reason)

    return var_name, values


def _get_value_by_path(state, var_name, required_by_attr_path):
    i = var_name.find(".")
    if i < 0:
        resource_name = var_name
    else:
        resource_name = var_name[:i]

    def _raise(e):
        msg = f"Plugin error: '{var_name}' does not exist in the output of resource '{resource_name}', which is required by '{required_by_attr_path}'"
        raise PlanException(msg) from e

    if resource_name in state["resources"]:
        try:
            return data_util.deep_get_attr(state, "output." + var_name)
        except Exception as e:
            _raise(e)
    if resource_name in state:
        try:
            return data_util.deep_get_attr(state, var_name)
        except Exception as e:
            _raise(e)


def _get_value_by_path2(state, var_name):
    i = var_name.find(".")
    if i < 0:
        resource_name = var_name
    else:
        resource_name = var_name[:i]

    if resource_name in state["resources"] or resource_name in state["runtimes"] or resource_name in state["providers"]:
        try:
            return data_util.deep_get_attr(state, "output." + var_name), True
        except Exception as e:
            log.debug(e)
            return None, False

    if resource_name in state:
        try:
            return data_util.deep_get_attr(state, var_name), True
        except Exception as e:
            log.debug(e)
            return None, False
    return None, False


def _deploy_res(name, res, state):
    def fn_deploy1(handler, res_data: dict, res_state: dict, fn_set_state: typing.Callable, kop: KOP):
        if _is_runtime(res):
            kop.start(KOP.MODE.create, handler.eta("create", res_data, state))
            new_state = handler.process(res_data, deepcopy(state))
            if new_state:
                fn_set_state(new_state)
            return

        if not res_state:
            action = actions.create
        else:
            action = handler.decide(res_data, res_state)

        if action == actions.skip:
            kop.skip("Already deployed")
            return

        if action == actions.recreate:
            with KOP(state, res["kind"], name) as kop2:
                kop2.id(res_state.get("id"))
                kop2.start(KOP.MODE.delete, handler.eta(actions.delete, res_data, res_state))
                handler.destroy(res_data, res_state, False)
            action = actions.create

        new_state = None
        if action == actions.create or action == None:
            kop.start(KOP.MODE.create, handler.eta(actions.create, res_data, res_state))
            if _has_save_state(handler.deploy):
                new_state = handler.deploy(res_data, res_state, fn_set_state)
            else:
                new_state = handler.deploy(res_data, res_state)
            kop.id(_discover_id(new_state))
        elif action == actions.update:
            kop.id(res_state.get("id"))
            kop.start(KOP.MODE.update, handler.eta(actions.update, res_data, res_state))
            if _has_save_state(handler.update):
                new_state = handler.update(res_data, res_state, fn_set_state)
            else:
                new_state = handler.update(res_data, res_state)
        else:
            raise PlanException(
                f"Unknown action. This is a problem of the concrete plugin.decide function. Plugin={name}, action={action}"
            )

        if new_state:
            fn_set_state(new_state)

    _handle_resource(name, res, state, True, fn_deploy1)


def _is_runtime(res):
    return "impl" in res


def _has_save_state(fn):
    signature = inspect.signature(fn)
    args = list(signature.parameters.keys())
    if len(args) < 3:
        return False
    name = args[2]
    if name == "save_state":
        return True
    p = signature.parameters[args[2]]
    return p.annotation == typing.Callable


def _assert_all_vars_resolved(data, name):
    def fn_on_value(path, value):
        if isinstance(value, str) and value.find("${") >= 0:
            raise PlanException(f"Unresolved variable '{path}' for plugin '{name}'. Value={value}")
        return value

    data_util.deep_update_object_value(data, fn_on_value)


_providers = {}
_provider_lock = threading.Lock()


def _ensure_provider(provider_id: str, state: dict):
    # Ensure provider initialized
    with _provider_lock:
        if not provider_id in _providers:
            provider = import_module("vhcs.plan.provider." + provider_id)
            # Get provider data
            meta = state["providers"].get(provider_id)

            def _get_value(path):
                return _get_value_by_path2(state, path)

            data_util.process_variables(meta, _get_value)

            data = meta.get("data") if meta else None
            if data:
                _assert_all_vars_resolved(data, provider_id)
            else:
                data = {}
            log.debug("[init] Provider: %s", provider_id)
            state["output"][provider_id] = provider.prepare(data)
            log.debug("[ok  ] Provider: %s", provider_id)
            _providers[provider_id] = 1


def _get_resource_handler(kind: str, state: dict):
    provider_id, res_handler_type = kind.split("/")
    res_handler_type = res_handler_type.replace("-", "_")
    _ensure_provider(provider_id, state)
    module_name = f"vhcs.plan.provider.{provider_id}.{res_handler_type}"
    return import_module(module_name)


def _get_runtime_handler(impl_name: str):
    return import_module(impl_name)


def get_common_items(iter1, iter2):
    return set(iter1).intersection(set(iter2))


def _handle_resource(name, res, state, for_deploy: bool, fn_process: typing.Callable):
    if "kind" in res:
        kind = res["kind"]
    elif "impl" in res:
        kind = "runtime"
    else:
        raise PlanException("Invalid definition. Neither kind nor impl attribute found. Resource name: " + name)

    kop_mode = KOP.MODE.create if for_deploy else KOP.MODE.delete
    with KOP(state, kind, name, kop_mode) as kop:

        def _get_value(path):
            return _get_value_by_path2(state, path)

        conditions = res.get("conditions")
        if conditions:
            conditions = deepcopy(conditions)
            ret = data_util.process_variables(conditions, _get_value)
            unsatisfied_condition_name = _get_unsatisfied_condition_name(conditions)
            if unsatisfied_condition_name:
                kop.skip("Condition not met: " + unsatisfied_condition_name)
                return

        # resolve vars
        data = res.get("data", {})
        if data:
            data = deepcopy(data)
            ret = data_util.process_variables(data, _get_value)
            if for_deploy:
                if ret["pending"]:
                    msg = f"Fail resolving variables for resource '{name}'. Unresolvable variables: {ret['pending']}"
                    raise PlanException(msg)
        state["resources"][name] = dict(res)
        state["resources"][name]["data"] = data

        if kind == "runtime":
            handler = _get_runtime_handler(res["impl"])
        else:
            handler = _get_resource_handler(kind, state)

        def _handle_resource_1(resource_data, resource_state, fn_set_state, kop) -> bool:
            if _is_runtime(res):  # runtime has no refresh
                pass
            else:
                new_state = handler.refresh(resource_data, resource_state)
                fn_set_state(new_state)
                resource_state = new_state

            fn_process(handler, resource_data, resource_state, fn_set_state, kop)

        for_var_name, values = _parse_statement_for(name, state)
        if for_var_name:
            if for_var_name in data:
                raise PlanException(
                    f"Invalid blueprint: variable name defined in for-statement already exists in data declaration. Resource: {name}. Conflicting names: {for_var_name}"
                )
            kop.id("(group)")
            kop.start()
            size = len(values)
            # ensure output array placeholder
            output = state["output"].get(name)
            if not output:
                output = []
                state["output"][name] = output
            while len(output) < size:
                output.append(None)
            for i in range(size):
                v = values[i]
                with KOP(state, kind, name + f"#{i}", kop_mode) as kop_per_item:
                    kop_per_item.id(str(i))
                    resource_state = output[i]

                    def _fn_set_state(o):
                        output[i] = deepcopy(o)

                    resource_data = deepcopy(data)
                    resource_data[for_var_name] = v
                    if v == None:
                        kop_per_item.skip("No input data")
                    else:
                        _handle_resource_1(resource_data, resource_state, _fn_set_state, kop_per_item)
        else:
            resource_state = state["output"].get(name)

            def _fn_set_state(o):
                state["output"][name] = deepcopy(o)

            resource_data = deepcopy(data)
            _handle_resource_1(resource_data, resource_state, _fn_set_state, kop)


def _get_unsatisfied_condition_name(conditions):
    if not conditions:
        return
    for condition_name, expr in conditions.items():
        if not expr:
            return condition_name
        if isinstance(expr, str):
            if expr.find("${") >= 0:  # still have unresolved variables
                return condition_name
        # expr could be an object. It's already "True". So skip.


def _discover_id(obj):
    if isinstance(obj, dict):
        return obj.get("id")


def _destroy_res(name, res_node, state, force):
    def fn_destroy1(handler, res_data: dict, res_state: dict, fn_set_state: typing.Callable, kop: KOP):
        if not res_state:
            kop.skip("Not found")
            return
        kop.id(_discover_id(res_state))
        kop.start(KOP.MODE.delete, handler.eta(actions.delete, res_data, res_state))
        ret = handler.destroy(res_data, res_state, force)
        state["destroy_output"][name] = deepcopy(ret)

        if _is_runtime(res_node):
            # No set empty data for runtime. Runtime is special and normally the data needs to be referenced in the next run.
            pass
        else:
            fn_set_state(None)

    _handle_resource(name, res_node, state, False, fn_destroy1)


def destroy(
    data,
    force: bool,
    target_resource_name: str = None,
    include_dependencies: bool = True,
    concurrency: int = 4,
    additional_context: dict = None,
):
    blueprint, state, state_file = _prepare_data(data, additional_context, target_resource_name)
    state["log"]["delete"] = []  # clear destroy log

    def destroy_resource(node_name):
        # ignore functional nodes (defaults, providers)
        node = blueprint["resources"].get(node_name)
        if not node:
            node = blueprint["runtimes"].get(node_name)

        if not node:
            return dag.walker.next

        _destroy_res(node_name, node, state, force)
        data_util.save_data_file(state, state_file)
        return dag.walker.next

    try:
        dag.process_blueprint(
            blueprint=blueprint,
            fn_process_node=destroy_resource,
            continue_on_error=force,
            reverse=True,
            concurrency=concurrency,
            target_node_name=target_resource_name,
            include_dependencies=include_dependencies,
        )
    except CalledProcessError as e:
        raise PlanException(str(e))
    finally:
        data_util.save_data_file(state, state_file)


def graph(
    data: dict,
    additional_context: dict = None,
    reverse: bool = False,
    target_resource: str = None,
    include_dependencies: bool = True,
):
    blueprint, state, state_file = _prepare_data(data, additional_context, None)
    g = dag.graph(blueprint, state, reverse, target_resource, include_dependencies)
    return g
