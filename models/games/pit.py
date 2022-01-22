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


class Pit:

    def __init__(self, json):

        profile = checkJsonNullValue(eval(json), 'profile')
        stats = checkJsonNullValue(eval(json), 'pit_stats_ptl')

        self.cash = checkJsonNullValue(eval(profile), 'cash')
        self.first_perk = checkJsonNullValue(eval(profile), 'selected_perk_0')
        self.second_perk = checkJsonNullValue(eval(profile), 'selected_perk_1')
        self.third_perk = checkJsonNullValue(eval(profile), 'selected_perk_2')
        self.genesis_allegiance = checkJsonNullValue(eval(profile), 'genesis_allegiance')
        self.genesis_points = checkJsonNullValue(eval(profile), 'genesis_points')
        self.first_killstreak = checkJsonNullValue(eval(profile), 'selected_killstreak_0')
        self.second_killstreak = checkJsonNullValue(eval(profile), 'selected_killstreak_1')
        self.third_killstreak = checkJsonNullValue(eval(profile), 'selected_killstreak_2')
        self.xp = checkJsonNullValue(eval(profile), 'xp')

        self.arrow_hits = checkJsonNullValue(eval(stats), 'arrow_hits')
        self.arrows_fired = checkJsonNullValue(eval(stats), 'arrows_fired')
        self.assists = checkJsonNullValue(eval(stats), 'assists')
        self.bow_damage_dealt = checkJsonNullValue(eval(stats), 'bow_damage_dealt')
        self.cash_earned = checkJsonNullValue(eval(stats), 'cash_earned')
        self.damage_dealt = checkJsonNullValue(eval(stats), 'damage_dealt')
        self.damage_received = checkJsonNullValue(eval(stats), 'damage_received')
        self.deaths = checkJsonNullValue(eval(stats), 'deaths')
        self.joins = checkJsonNullValue(eval(stats), 'joins')
        self.pit_jump = checkJsonNullValue(eval(stats), 'jumped_into_pit')
        self.left_clicks = checkJsonNullValue(eval(stats), 'left_clicks')
        self.melee_damage_dealt = checkJsonNullValue(eval(stats), 'melee_damage_dealt')
        self.melee_damage_received = checkJsonNullValue(eval(stats), 'melee_damage_received')
        self.playtime = checkJsonNullValue(eval(stats), 'playtime_minutes')
        self.sword_hits = checkJsonNullValue(eval(stats), 'sword_hits')
        self.bow_damage_received = checkJsonNullValue(eval(stats), 'bow_damage_received')
        self.gapple_eaten = checkJsonNullValue(eval(stats), 'gapple_eaten')
        self.launchers_launch = checkJsonNullValue(eval(stats), 'launched_by_launchers')
        self.blocks_placed = checkJsonNullValue(eval(stats), 'blocks_placed')
        self.ghead_eaten = checkJsonNullValue(eval(stats), 'ghead_eaten')
        self.blocks_broken = checkJsonNullValue(eval(stats), 'blocks_broken')
