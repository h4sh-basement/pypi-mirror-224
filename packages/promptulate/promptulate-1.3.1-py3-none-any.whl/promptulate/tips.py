# Copyright (c) 2023 promptulate
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Copyright Owner: Zeeland
# GitHub Link: https://github.com/Undertone0809/
# Project Link: https://github.com/Undertone0809/promptulate
# Contact Email: zeeland@foxmail.com

from typing import Optional

__all__ = ["EmptyMessageSetError", "OpenAIError", "NetWorkError"]


class EmptyMessageSetError(Exception):
    pass


class OpenAIError(Exception):
    def __init__(self, msg: str):
        super().__init__(f"<OpenAI> could not get data correctly, reasons: {msg}")


class NetWorkError(Exception):
    def __init__(self, origin: str, reason: Optional[str] = None):
        msg = f"<{origin}> could not get data"
        if reason:
            msg += f", reason: {reason}"
        super().__init__(msg)
