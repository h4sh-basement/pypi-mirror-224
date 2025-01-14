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



def process(data: dict, state: dict) -> dict:
    n = data["n"]
    return {
        'fibonacci': _fibonacci(n)
    }

def _fibonacci(n: int):
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if n == 1:
        return 0
    if n == 2:
        return 1

    prev, curr = 0, 1
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr

def destroy(data: dict, state: dict, force: bool) -> dict:
    return

def eta(action: str, data: dict, state: dict):
    return "10s"
