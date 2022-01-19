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


class Arcade:

    def __init__(self, json):
        self.coins = checkJsonNullValue(eval(json), 'coins')
        self.wins_dayone = checkJsonNullValue(eval(json), 'wins_dayone')
        self.wins_mini_walls = checkJsonNullValue(eval(json), 'wins_mini_walls')
        self.miniwalls_active_kit = checkJsonNullValue(eval(json), 'miniwalls_activeKit')
        self.wins_soccer = checkJsonNullValue(eval(json), 'wins_soccer')
        self.rounds_simon_says = checkJsonNullValue(eval(json), 'rounds_simon_says')
        self.rounds_hole_in_the_wall = checkJsonNullValue(eval(json), 'rounds_hole_in_the_wall')
        self.melee_weapon = checkJsonNullValue(eval(json), 'melee_weapon')
        self.cosmetics = checkJsonNullValue(eval(json), 'packages')
        self.wins_farm_hunt = checkJsonNullValue(eval(json), 'wins_farm_hunt')
        self.hider_wins_hide_and_seek = checkJsonNullValue(eval(json), 'hider_wins_hide_and_seek')
        self.best_round_zombies = checkJsonNullValue(eval(json), 'best_round_zombies')
        self.seeker_wins_hide_and_seek = checkJsonNullValue(eval(json), 'seeker_wins_hide_and_seek')
        self.wins_zombies = checkJsonNullValue(eval(json), 'wins_zombies')
        self.wins_party = checkJsonNullValue(eval(json), 'wins_party')
        self.wins_hole_in_the_wall = checkJsonNullValue(eval(json), 'wins_hole_in_the_wall')
        self.wins_simon_says = checkJsonNullValue(eval(json), 'wins_simon_says')
        self.wins_oneinthequiver = checkJsonNullValue(eval(json), 'wins_oneinthequiver')
        self.enderspleef_trail = checkJsonNullValue(eval(json), 'enderspleef_trail')
        self.bounty_head = checkJsonNullValue(eval(json), 'bounty_head')
        self.wins_ender = checkJsonNullValue(eval(json), 'wins_ender')
        self.wins_dragonwars2 = checkJsonNullValue(eval(json), 'wins_dragonwars2')
        self.wins_draw_their_thing = checkJsonNullValue(eval(json), 'wins_draw_their_thing')
        self.wins_throw_out = checkJsonNullValue(eval(json), 'wins_throw_out')
