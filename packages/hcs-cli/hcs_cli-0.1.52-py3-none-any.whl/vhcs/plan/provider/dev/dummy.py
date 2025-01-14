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

import time
from copy import deepcopy
from typing import Callable
import vhcs.ctxp.duration as duration
from vhcs.plan import actions
from vhcs.plan import PluginException


def deploy(data: dict, state: dict, save_state: Callable) -> dict:
    text = data.get("text")
    error = data.get("error")
    delay = data.get("delay")
    a = data.get("a", 0)
    b = data.get("b", 0)
    error_before_save = data.get("error_before_save")
    delay_seconds = duration.to_seconds(delay)
    if delay_seconds:
        time.sleep(delay_seconds)
    ret = deepcopy(data)
    ret["outputText"] = text
    ret["n"] = a + b

    if not error_before_save:
        save_state(ret)

    if error:
        raise PluginException(error)

    return ret


def refresh(data: dict, state: dict) -> dict:
    return state


def decide(data: dict, state: dict):
    return actions.skip


def destroy(data: dict, state: dict, force: bool) -> dict:
    return {}


def eta(action: str, data: dict, state: dict):
    if action == actions.create:
        return "10s"
    if action == actions.delete:
        return "10s"
