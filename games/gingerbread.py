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


class GingerBread:

    def __init__(self, json):
        self.cosmetics = checkJsonNullValue(eval(json), 'packages')
        self.helmet = checkJsonNullValue(eval(json), 'helmet_active')
        self.jacket = checkJsonNullValue(eval(json), 'jacket_active')
        self.pants = checkJsonNullValue(eval(json), 'pants_active')
        self.shoes = checkJsonNullValue(eval(json), 'shoes_active')
        self.skin = checkJsonNullValue(eval(json), 'skin_active')
        self.coins = checkJsonNullValue(eval(json), 'coins')
        self.box_pickups = checkJsonNullValue(eval(json), 'box_pickups')
        self.coins_picked_up = checkJsonNullValue(eval(json), 'coins_picked_up')
        self.laps = checkJsonNullValue(eval(json), 'laps_completed')
        self.bronze_trophies = checkJsonNullValue(eval(json), 'bronze_trophy')
        self.wins = checkJsonNullValue(eval(json), 'wins')
        self.gold_trophies = checkJsonNullValue(eval(json), 'gold_trophy')
        self.silver_trophies = checkJsonNullValue(eval(json), 'silver_trophy')
        self.prefix_color = checkJsonNullValue(eval(json), 'prefix_color')
        self.particle_trail = checkJsonNullValue(eval(json), 'particle_trail')
