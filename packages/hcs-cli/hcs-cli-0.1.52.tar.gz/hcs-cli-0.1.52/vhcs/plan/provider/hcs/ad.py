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

from vhcs.plan import actions
from vhcs.service import admin


def deploy(data: dict, state: dict) -> dict:
    label = data["providerLabel"]
    return admin.ad.create(label, data)


def refresh(data: dict, state: dict) -> dict:
    org_id = data["orgId"]
    if state:
        id = state.get("id")
        if id:
            return admin.ad.get(id, org_id)

    # Fall back with smart find by name
    search = "name $eq " + data["name"]
    ads = admin.ad.list(org_id=org_id, search=search)
    if ads:
        return ads[0]


def decide(data: dict, state: dict):
    return actions.skip


def destroy(data: dict, state: dict, force: bool) -> dict:
    org_id = data["orgId"]
    id = state["id"]
    return admin.ad.delete(id, org_id)


def eta(action: str, data: dict, state: dict):
    if action == actions.create:
        return "1m"
    if action == actions.delete:
        return "1m"
