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


class Quake:

    def __init__(self, json):
        self.barrel = checkJsonNullValue(eval(json), 'barrel')
        self.case = checkJsonNullValue(eval(json), 'case')
        self.coins = checkJsonNullValue(eval(json), 'coins')
        self.deaths = checkJsonNullValue(eval(json), 'deaths')
        self.kills = checkJsonNullValue(eval(json), 'kills')
        self.kill_sound = checkJsonNullValue(eval(json), 'killsound')
        self.killstreaks = checkJsonNullValue(eval(json), 'killstreaks')
        self.muzzle = checkJsonNullValue(eval(json), 'muzzle')
        self.cosmetics = checkJsonNullValue(eval(json), 'packages')
        self.sight = checkJsonNullValue(eval(json), 'sight')
        self.trigger = checkJsonNullValue(eval(json), 'trigger')
        self.wins = checkJsonNullValue(eval(json), 'wins')
        self.dash_cooldown = checkJsonNullValue(eval(json), 'dash_cooldown')
        self.dash_power = checkJsonNullValue(eval(json), 'dash_power')
        self.headshots = checkJsonNullValue(eval(json), 'headshots')
        self.distance_travelled = checkJsonNullValue(eval(json), 'distance_travelled')
        self.shots_fired = checkJsonNullValue(eval(json), 'shots_fired')
        self.beam = checkJsonNullValue(eval(json), 'beam')
        self.kill_prefix = checkJsonNullValue(eval(json), 'selectedKillPrefix')
