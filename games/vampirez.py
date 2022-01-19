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


class VampireZ:

    def __init__(self, json):
        self.coins = checkJsonNullValue(eval(json), 'coins')
        self.human_deaths = checkJsonNullValue(eval(json), 'human_deaths')
        self.human_kills = checkJsonNullValue(eval(json), 'human_kills')
        self.human_wins = checkJsonNullValue(eval(json), 'human_wins')
        self.vampire_deaths = checkJsonNullValue(eval(json), 'vampire_deaths')
        self.vampire_kills = checkJsonNullValue(eval(json), 'vampire_kills')
        self.zombie_kills = checkJsonNullValue(eval(json), 'zombie_kills')
        self.cosmetics = checkJsonNullValue(eval(json), 'packages')
        self.gold_bought = checkJsonNullValue(eval(json), 'gold_bought')
        self.vampire_wins = checkJsonNullValue(eval(json), 'vampire_wins')
        self.vampire_color = checkJsonNullValue(eval(json), 'vamp_color')
