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

from utils import checkJsonNullValue


class APIKey:

    def __init__(self, json):

        true = True
        false = False

        self.success = checkJsonNullValue(eval(json), 'success')

        record = checkJsonNullValue(eval(json), 'record')

        self.key = checkJsonNullValue(eval(record), 'key')
        self.owner = checkJsonNullValue(eval(record), 'owner')
        self.limit = checkJsonNullValue(eval(record), 'limit', 120)
        self.queries_in_past_minute = checkJsonNullValue(eval(record), 'queriesInPastMin', 0)
        self.total_queries = checkJsonNullValue(eval(record), 'totalQueries', 0)
