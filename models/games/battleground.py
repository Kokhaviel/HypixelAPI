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


class BattleGround:

    def __init__(self, json):
        self.chosen_class = checkJsonNullValue(eval(json), 'chosen_class')
        self.coins = checkJsonNullValue(eval(json), 'coins')
        self.damage = checkJsonNullValue(eval(json), 'damage')
        self.deaths = checkJsonNullValue(eval(json), 'deaths')
        self.heal = checkJsonNullValue(eval(json), 'heal')
        self.kills = checkJsonNullValue(eval(json), 'kills')
        self.losses = checkJsonNullValue(eval(json), 'losses')
        self.magic_dust = checkJsonNullValue(eval(json), 'magic_dust')
        self.cosmetics = checkJsonNullValue(eval(json), 'packages')
        self.repaired = checkJsonNullValue(eval(json), 'repaired')
        self.void_shards = checkJsonNullValue(eval(json), 'void_shards')
        self.wins = checkJsonNullValue(eval(json), 'wins')
        self.assists = checkJsonNullValue(eval(json), 'assists')
