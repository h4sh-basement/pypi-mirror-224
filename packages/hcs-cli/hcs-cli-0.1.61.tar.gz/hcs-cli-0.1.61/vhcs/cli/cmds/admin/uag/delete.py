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

import httpx
import click
from vhcs.service import admin
import vhcs.sglib.cli_options as cli


@click.command()
@click.argument("id", type=str, required=True)
@cli.org_id
@cli.wait
def delete(id: str, org: str, wait: str):
    """Delete UAG by ID"""

    org_id = cli.get_org_id(org)
    try:
        ret = admin.uag.delete(id, org_id)
        if not ret:
            return "", 1
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 409:
            pass
        else:
            raise
    if wait == "0":
        return ret
    admin.uag.wait_for_deleted(id, org_id, wait)
