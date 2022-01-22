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


class Smash:

    def __init__(self, json):
        self.coins = checkJsonNullValue(eval(json), 'coins')
        self.class_ = checkJsonNullValue(eval(json), 'active_class')
        self.smasher = checkJsonNullValue(eval(json), 'smasher')
        self.kills = checkJsonNullValue(eval(json), 'kills')
        self.wins = checkJsonNullValue(eval(json), 'wins')
        self.damage_dealt = checkJsonNullValue(eval(json), 'damage_dealt')
        self.smashed = checkJsonNullValue(eval(json), 'smashed')
        self.deaths = checkJsonNullValue(eval(json), 'deaths')
        self.games_played = checkJsonNullValue(eval(json), 'games')
        self.losses = checkJsonNullValue(eval(json), 'losses')
        self.quits = checkJsonNullValue(eval(json), 'quits')
        self.assists = checkJsonNullValue(eval(json), 'assists')
