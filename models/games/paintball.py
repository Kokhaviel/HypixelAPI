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


class Paintball:

    def __init__(self, json):
        self.adrenaline = checkJsonNullValue(eval(json), 'adrenaline')
        self.coins = checkJsonNullValue(eval(json), 'coins')
        self.deaths = checkJsonNullValue(eval(json), 'deaths')
        self.endurance = checkJsonNullValue(eval(json), 'endurance')
        self.fortune = checkJsonNullValue(eval(json), 'fortune')
        self.godfather = checkJsonNullValue(eval(json), 'godfather')
        self.kills = checkJsonNullValue(eval(json), 'kills')
        self.cosmetics = checkJsonNullValue(eval(json), 'packages')
        self.shots_fired = checkJsonNullValue(eval(json), 'shots_fired')
        self.super_luck = checkJsonNullValue(eval(json), 'superluck')
        self.transfusion = checkJsonNullValue(eval(json), 'transfusion')
        self.wins = checkJsonNullValue(eval(json), 'wins')
        self.hat = checkJsonNullValue(eval(json), 'hat')
