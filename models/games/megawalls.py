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


class MegaWalls:

    def __init__(self, json):
        self.assists = checkJsonNullValue(eval(json), 'assists')
        self.chosen_class = checkJsonNullValue(eval(json), 'chosen_class')
        self.coins = checkJsonNullValue(eval(json), 'coins')
        self.deaths = checkJsonNullValue(eval(json), 'deaths')
        self.final_deaths = checkJsonNullValue(eval(json), 'finalDeaths')
        self.final_kills = checkJsonNullValue(eval(json), 'finalKills')
        self.kills = checkJsonNullValue(eval(json), 'kills')
        self.losses = checkJsonNullValue(eval(json), 'losses')
        self.cosmetics = checkJsonNullValue(eval(json), 'packages')
        self.cry = checkJsonNullValue(eval(json), 'war_cry')
        self.wins = checkJsonNullValue(eval(json), 'wins')
        self.wither_damage = checkJsonNullValue(eval(json), 'witherDamage')
        self.time_played = checkJsonNullValue(eval(json), 'time_played')
        self.fallen = checkJsonNullValue(eval(json), 'meters_fallen')
        self.walked = checkJsonNullValue(eval(json), 'meters_walked')
        self.games_played = checkJsonNullValue(eval(json), 'games_played')
        self.damage_dealt = checkJsonNullValue(eval(json), 'damage_dealt')
        self.potions_drunk = checkJsonNullValue(eval(json), 'potions_drunk')
        self.blocks_broken = checkJsonNullValue(eval(json), 'blocks_broken')
        self.blocks_placed = checkJsonNullValue(eval(json), 'blocks_placed')
        self.wither_kills = checkJsonNullValue(eval(json), 'wither_kills')
