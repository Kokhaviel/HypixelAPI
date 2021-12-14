#  Copyright (c) 2021 Kokhaviel.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import requests

from key import APIKey


class HypixelAPI:
    api_key = ""
    base_url = "https://api.hypixel.net/"

    def __init__(self, api_key):
        self.api_key = api_key

    def getAPIKeyInfo(self):
        if self.api_key == "":
            raise HypixelAPIException("You Must Defined an API Key with __init__")
        json = requests.get(self.base_url + "key", params={"key": self.api_key}).json()
        return APIKey(json)


class HypixelAPIException(Exception):

    def __init__(self, message):
        self.message = message

