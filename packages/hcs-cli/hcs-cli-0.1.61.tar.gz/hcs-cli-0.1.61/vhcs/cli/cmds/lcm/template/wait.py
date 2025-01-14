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

import click
from vhcs.service import lcm
from vhcs.util import duration


@click.command()
@click.argument("id", type=str, required=True)
@click.option(
    "--status",
    "-s",
    type=click.Choice(["READY", "ERROR", "DELETING", "EXPANDING", "SHRINKING", "CUSTOMIZING", "MAINTENANCE"]),
    required=False,
    default="READY",
    help="The target status to wait for.",
)
@click.option("--timeout", "-t", type=str, required=False, default="1m", help="Timeout. Examples: '2m', '30s', '1h30m'")
@click.option(
    "--fail-fast/--fail-timeout-only",
    "-f",
    type=bool,
    default=True,
    required=False,
    help="Stop waiting if the template reached to non-expected terminal states, e.g. waiting for ERROR but template is READY, or waiting for READY and template is ERROR.",
)
@click.option(
    "--silent/--return-template",
    type=bool,
    required=False,
    default=True,
    help="Slient mode will has no output on success. Otherwise the full template is returned",
)
def wait(id: str, status: str, timeout: str, fail_fast: bool, silent: bool):
    """Wait for a template to transit to specific status. If the template"""

    timeout_seconds = duration.to_seconds(timeout)
    expected_status = status.upper().split(",")
    exclude_status = []
    if fail_fast:
        if "READY" not in expected_status:
            exclude_status.append("READY")
        if "ERROR" not in expected_status:
            exclude_status.append("ERROR")
    try:
        template = lcm.template.wait(id, timeout_seconds, expected_status, exclude_status)
        return template if not silent else None
    except Exception as e:
        return str(e), 1
