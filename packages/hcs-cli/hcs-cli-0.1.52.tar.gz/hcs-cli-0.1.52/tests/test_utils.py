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

import subprocess
import json
from unittest import TestCase


def _run(cmd: str, stdin_payload: str = None):
    p = subprocess.run(cmd, input=stdin_payload, shell=True, text=True, check=False, capture_output=True)
    return p.stdout, p.stderr, p.returncode


_test_profile_name = "__ctxp_ut"


def _create_test_profile():
    cmd = f"hcs profile create {_test_profile_name}"
    p = subprocess.Popen(cmd, shell=True, text=True, stdin=subprocess.PIPE)
    p.communicate(input='{"a":1}')
    p.wait()


def _delete_test_profile():
    _run(f"hcs profile delete {_test_profile_name}")


class CliTest(TestCase):
    @classmethod
    def setUpClass(cls):
        _delete_test_profile()
        _create_test_profile()

    @classmethod
    def tearDownClass(cls):
        _delete_test_profile()

    @classmethod
    def NON_EMPTY_STRING(cls, data):
        if data is None or len(data) == 0:
            raise Exception("Expect non-empty output, but got empty.")

    @classmethod
    def NON_EMPTY_JSON(cls, data):
        if data is None or len(data) == 0:
            raise Exception("Expect non-empty json, but got empty.")
        d = json.loads(data)
        if len(d) == 0:
            raise Exception("Expect non-empty json, but got empty dict.")

    def verify(
        self,
        cmd: str,
        expected_data: any,
        expected_return_code: int = 0,
        expect_stderr_empty: bool = True,
        stdin_payload: str = None,
    ):
        stdout, stderr, returncode = _run(cmd, stdin_payload)
        try:
            # verify return code
            self.assertEqual(returncode, expected_return_code, "Invalid return code.")

            # verify stderr
            actual_stderr_empty = stderr is None or len(stderr) == 0
            self.assertEqual(
                expect_stderr_empty,
                actual_stderr_empty,
                f"Invalid stderr. Expect empty={expect_stderr_empty}, actual={stderr}",
            )

            # verify output
            t = type(expected_data)
            if expected_data is None or t is str:
                self.assertEqual(expected_data, stdout, "stdout mismatch")
            elif callable(expected_data):
                expected_data(stdout)
            elif t is dict or t is list:
                if stdout is None:
                    self.fail("Expect stdout but got None")
                else:
                    data = json.loads(stdout)
                    self.assertEqual(expected_data, data)
            else:
                raise Exception(
                    f"type of expected_data must be dict, string, or function. Current type: {t}. This is an error of the test case."
                )
        except Exception:
            print("<DUMP STDOUT>", stdout)
            print("<DUMP STDERR>", stderr)
            raise
