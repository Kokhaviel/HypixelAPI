#  Copyright (c) 2022 Kokhaviel.
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

from utils import checkJsonNullValue
import json


class Friends:

    def __init__(self, json_contents):

        true = True
        false = False

        self.success = checkJsonNullValue(eval(json_contents), 'success')
        self.uuid = checkJsonNullValue(eval(json_contents), 'uuid')
        records = checkJsonNullValue(eval(json_contents), 'records')
        friends_json = json.loads(records.replace("\'", "\""))

        self.friends = []
        for friend in friends_json:
            self.friends.append(Friend(str(friend)))


class Friend:

    def __init__(self, json_contents):
        self.id = checkJsonNullValue(eval(json_contents), '_id')
        self.uuid_sender = checkJsonNullValue(eval(json_contents), 'uuidSender')
        self.uuid_receiver = checkJsonNullValue(eval(json_contents), 'uuidReceiver')
        self.started = checkJsonNullValue(eval(json_contents), 'started')
