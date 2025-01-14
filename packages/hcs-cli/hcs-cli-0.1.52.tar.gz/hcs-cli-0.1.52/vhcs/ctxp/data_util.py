from os import path
from typing import Tuple, Any
import json
import yaml
import re
from .util import CtxpException


def load_data(file_name: str, class_type: str):
    data = load_data_file(file_name)
    if data == None:
        return
    return strict_dict_to_class(data, class_type)


def load_data_file(file_name: str, default=None, format="auto") -> dict | str | None:
    if not path.exists(file_name) or not path.isfile(file_name):
        return default

    with open(file_name, encoding="utf-8") as file:
        text = file.read()

    _, ext = path.splitext(file_name)
    if ext == ".json" or format == "json":
        if format != "auto" and format != "json":
            raise CtxpException(f"File extension does not match specified format. File={file_name}, format={format}")
        data = json.loads(text)
        return default if data == None else data  # handle empty file
    if ext == ".yaml" or ext == ".yml" or format == "yml" or format == "yaml":
        if format != "auto" and format != "yaml" and format != "yml":
            raise CtxpException(f"File extension does not match specified format. File={file_name}, format={format}")
        data = yaml.safe_load(text)
        return default if data == None else data  # handle empty file
    return text


def save_data_file(data: dict | list, file_name: str, format: str = "yaml"):
    with open(file_name, "w") as file:
        if format == "yaml":
            # TODO
            # yaml.safe_dump(data, file, sort_keys=False)
            yaml.safe_dump(json.loads(json.dumps(data, default=vars)), file, sort_keys=False)
        elif format == "json":
            json.dump(data, file, indent=4, default=vars)
        else:
            raise CtxpException("Invalid format: " + format)


def strict_dict_to_class(data: dict, class_type):
    actual_keys = set(data.keys())
    declared_keys = set(class_type.__annotations__.keys())
    unexpected_fields = actual_keys - declared_keys
    if unexpected_fields:
        raise ValueError(f"Unexpected fields: {unexpected_fields} while deserializing class {class_type.__name__}")

    mandatory_keys = set()
    for k in declared_keys:
        if not hasattr(class_type, k):
            mandatory_keys.add(k)
    missing_fields = mandatory_keys - actual_keys
    if missing_fields:
        raise ValueError(f"Missing fields: {class_type.__name__}.{missing_fields}")

    inst = class_type()

    for field_name, field_type in class_type.__annotations__.items():
        value = data.get(field_name)
        if isinstance(value, field_type):
            setattr(inst, field_name, value)
            continue
        if isinstance(value, dict):
            value = strict_dict_to_class(value, field_type)
            setattr(inst, field_name, value)
            continue
        raise ValueError(
            f"Field '{class_type.__name__}.{field_name}' has an incorrect type. Declared: {field_type}, actual: {type(value)}"
        )
    return inst


def deep_update_object_value(obj, fn_change, _current_path: str = ""):
    if isinstance(obj, list):
        for i in range(len(obj)):
            obj[i] = deep_update_object_value(obj[i], fn_change, _current_path + f"[{i}]")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            item_path = _current_path + "." + k if _current_path else k
            obj[k] = deep_update_object_value(v, fn_change, item_path)
    else:
        obj = fn_change(_current_path, obj)
    return obj


def deep_apply_defaults(to_obj: dict, from_obj: dict) -> bool:
    """If a property in to_obj is empty, use the value from from_obj if the same property is not empty"""
    if not from_obj:
        return
    changed = False
    for k, v in to_obj.items():
        v1 = from_obj.get(k)
        if not v1:
            continue
        if not v:
            to_obj[k] = v1
            changed = True
            continue
        if isinstance(v, dict):
            if deep_apply_defaults(v, v1):
                changed = True
    return changed


def deep_get_attr(obj: dict, path: str):
    parts = path.split(".")
    for k in parts:
        try:
            obj = _get_obj_attr(obj, k)
        except KeyError:
            raise CtxpException("Property path not found: " + path)
    return obj


def deep_set_attr(obj: dict, path: str, value):
    parts = path.split(".")
    k = None
    try:
        for i in range(len(parts)):
            k = parts[i]
            obj = _get_obj_attr(obj, k)

            if i == len(parts) - 2:
                # found the one before the leaf.
                _set_obj_attr(obj, parts[i + 1], value)
                break
        return obj
    except (KeyError, TypeError, IndexError) as e:
        raise CtxpException(f"Property path error: {path}. Cause={e}, current={k}, i={i}")


def _get_obj_attr(o, k):
    name, array_index = _parse_array_property_name(k)

    if isinstance(o, dict):
        ret = o[name]
    else:
        ret = getattr(o, name)

    if array_index != None:
        ret = ret[array_index]

    return ret


def _set_obj_attr(o, k, v):
    name, array_index = _parse_array_property_name(k)
    if isinstance(o, dict):
        if array_index is None:
            o[name] = v
        else:
            o[name][array_index] = v
    else:
        if array_index is None:
            setattr(o, name, v)
        else:
            array_elem = getattr(o, name)
            array_elem[array_index] = v


_array_index_matcher = re.compile("(.+)\[(\d+)\]")


def _parse_array_property_name(k: str) -> Tuple[str, int]:
    m = _array_index_matcher.match(k)
    if m:
        return m.group(1), int(m.group(2))
    return k, None


def deep_iterate(obj, fn_on_value):
    if isinstance(obj, list) or isinstance(obj, set):
        for v in obj:
            deep_iterate(v, fn_on_value)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            deep_iterate(v, fn_on_value)
    else:
        fn_on_value(obj)


def deep_find_variables(obj):
    collector = set()

    def fn_on_value(v):
        if not v or not isinstance(v, str):
            return
        matches = re.findall(_pattern_var_only, v)
        if matches:
            m2 = _pattern_var_list.match(v)
            if m2:
                collector.add(m2.group(2))
            else:
                for i in matches:
                    collector.add(i)

    deep_iterate(obj, fn_on_value)
    return collector


def process_variables(obj: dict, fn_get_var=None):
    if fn_get_var == None:

        def _fn_get_var(name):
            try:
                return deep_get_attr(obj, name), True
            except:
                return None, False

        fn_get_var = _fn_get_var

    total_changed = {}
    while True:
        ret = _process_variables_impl(obj, fn_get_var)
        total_changed.update(ret["changed"])
        if not ret["changed"]:
            return {
                "data": ret["data"],
                "changed": total_changed,
                "pending": ret["pending"],
            }


_pattern_var = re.compile(".*\$\{(.+?)\}.*")
_pattern_var_only = re.compile("\$\{(.+?)\}")
_pattern_var_list = re.compile("\$\{\s*\[\s*for\s+(.+?)\s+in\s+(.+?)\s*\:\s*(.+)\s*]\s*\}")


def _process_variables_impl(obj: dict, fn_get_var=None):
    changed = {}
    pending = {}

    def fn_change(path, v):
        resolved, pending_var = resolve_expression(v, fn_get_var, path)
        if pending_var:
            pending[path] = pending_var
        elif resolved != v:
            changed[path] = v
        return resolved

    data = deep_update_object_value(obj, fn_change)
    return {"changed": changed, "pending": pending, "data": data}


def resolve_expression(expr, fn_get_value, referencing_attr_path) -> Tuple[Any, str]:
    """Try resolving expression. Returned updated value and None, or value and pending var name"""

    if not isinstance(expr, str):
        return expr, None
    # get variable names from expr
    m1 = _pattern_var.match(expr)
    if not m1:
        return expr, None
    m2 = _pattern_var_list.match(expr)
    if m2:
        # expression match
        tmp_var_name = m2.group(1)
        src_var_name = m2.group(2)
        mapped_value = m2.group(3)

        target_value, found = fn_get_value(src_var_name)
        if not found:
            return expr, src_var_name
        if not isinstance(target_value, list):
            raise CtxpException(
                f"Invalid variable value for expression. Expect list, actual {type(target_value).__name__}. attr_path={referencing_attr_path}, src_var_name={src_var_name}"
            )
        if not mapped_value.startswith(tmp_var_name + "."):
            raise CtxpException(
                f"Unsupported expression. attr_path={referencing_attr_path}, src_var_name={src_var_name}"
            )
        new_attr_path = mapped_value[len(tmp_var_name) + 1 :]
        ret = []
        for i in target_value:
            if i == None:
                # raise CtxpException(f"Invalid value encountered during processing array expansion expression. The value in the referenced array is None. This is normally a problem of the data, not the caller. attr_path={referencing_attr_path}, src_var_name={src_var_name}")
                # There are valid cases that some of such items are null. Raising exception
                # makes the handling hard. Pass-on null in such scenario, so enable the downstream
                # components to decide what to do with the null case.
                item = None
            else:
                item = deep_get_attr(i, new_attr_path)
            ret.append(item)
        return ret, None  # replace the entire value using the new value.
    else:
        var_name = m1.group(1)
        # string replacement
        actual_value, found = fn_get_value(var_name)
        if not found:
            return expr, var_name
        if isinstance(actual_value, str):
            return expr.replace("${" + var_name + "}", actual_value), None
        # replacement is an object. Make sure this var is the entire value.
        if len(expr) != len(var_name) + 3:
            raise CtxpException(
                f"Invalid variable: can not replace variable in string with non-string. attr_path={referencing_attr_path}, var_name={var_name}, replacement={actual_value}, expr={expr}"
            )
        return actual_value, None


def to_json(o) -> str:
    class SetEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, set):
                return list(obj)
            return json.JSONEncoder.default(self, obj)

    return json.dumps(o, cls=SetEncoder, indent=4)


def get_common_items(iter1, iter2):
    set1 = set(iter1)
    set2 = set(iter2)
    common_items = set1.intersection(set2)
    return common_items
