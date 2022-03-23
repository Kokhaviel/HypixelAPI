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


class RecentGames:

    def __init__(self, json_contents):

        true = True
        false = False

        self.success = checkJsonNullValue(eval(json_contents), 'success')
        self.uuid = checkJsonNullValue(eval(json_contents), 'uuid')
        records = checkJsonNullValue(eval(json_contents), 'games')

        games_json = json.loads(records.replace("\'", "\""))

        self.games = []
        for game in games_json:
            self.games.append(Game(str(game)))


class Game:

    def __init__(self, json_contents):
        self.started = checkJsonNullValue(eval(json_contents), 'date')
        self.type = checkJsonNullValue(eval(json_contents), 'gameType')
        self.mode = checkJsonNullValue(eval(json_contents), 'mode')
        self.map = checkJsonNullValue(eval(json_contents), 'map')
        self.ended = checkJsonNullValue(eval(json_contents), 'ended')
