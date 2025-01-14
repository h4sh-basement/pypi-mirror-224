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

from vhcs.ctxp import data_util
from vhcs.ctxp import config, profile, CtxpException

_hcs_envs = config.get("hcs-deployments.yaml")


def _is_production_env(hdc_url: str) -> bool:
    for env in _hcs_envs["prod"]:
        if env.hdc.url == hdc_url:
            return True


def _get_csp_url(hdc_url: str) -> str:
    if _is_production_env(hdc_url):
        return "https://console.cloud.vmware.com"
    return "https://console-stg.cloud.vmware.com"


def ensure_default_production_profile():
    doc = get_default_profile_template()
    _ensure_profile("default", doc, interactive=False)


def get_default_profile_template():
    stack_name = "prod-na-cp102"
    for stack in _hcs_envs["prod"]:
        if stack.env == stack_name:
            return _profile_data_from_stack(stack)
    raise CtxpException("Production configuration not found: " + stack_name)


def _profile_data_from_stack(stack):
    return {
        "hcs": {"url": stack.hdc.url, "regions": stack.regions},
        "csp": {
            "url": _get_csp_url(stack.hdc.url),
            "orgId": None,
            "apiToken": None,
            "clientId": None,
            "clientSecret": None,
        },
    }


def _ensure_profile(name, data, interactive: bool = True):
    existing = profile.get(name)
    if existing:
        if data_util.deep_apply_defaults(existing, data):
            profile.save(name, existing)
            if interactive:
                print("Profile created: " + name)
        else:
            if interactive:
                print("Profile unchanged: " + name)
    else:
        profile.create(name, data, False)
        if interactive:
            print("Profile created: " + name)


def ensure_dev_profiles():
    items = []
    items += _hcs_envs["prod"]
    items += _hcs_envs["staging"]
    items += _hcs_envs["dev"]

    for stack in items:
        name = stack.alias or stack.env
        doc = _profile_data_from_stack(stack)
        _ensure_profile(name, doc)
    _ensure_profile("nightly", profile.get("integration"))
