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


class Legacy:

    def __init__(self, json):
        self.channel = checkJsonNullValue(eval(json), 'preferredChannel')
        self.tokens = checkJsonNullValue(eval(json), 'tokens')
        self.total_tokens = checkJsonNullValue(eval(json), 'total_tokens')
        self.gingerbread_tokens = checkJsonNullValue(eval(json), 'gingerbread_tokens')
        self.walls_tokens = checkJsonNullValue(eval(json), 'walls_tokens')
        self.arena_tokens = checkJsonNullValue(eval(json), 'arena_tokens')
        self.quakecraft_tokens = checkJsonNullValue(eval(json), 'quakecraft_tokens')
        self.paintball_tokens = checkJsonNullValue(eval(json), 'paintball_tokens')
        self.vampirez_tokens = checkJsonNullValue(eval(json), 'vampirez_tokens')
