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


class MurderMystery:

    def __init__(self, json):
        self.wins = checkJsonNullValue(eval(json), 'wins')
        self.coins = checkJsonNullValue(eval(json), 'coins')
        self.knife_kills = checkJsonNullValue(eval(json), 'knife_kills')
        self.games_played = checkJsonNullValue(eval(json), 'games')
        self.kills = checkJsonNullValue(eval(json), 'kills')
        self.coins_picked_up = checkJsonNullValue(eval(json), 'coins_pickedup')
        self.deaths = checkJsonNullValue(eval(json), 'deaths')
        self.bow_kills = checkJsonNullValue(eval(json), 'bow_kills')
        self.detective_chance = checkJsonNullValue(eval(json), 'detective_chance')
        self.murderer_chance = checkJsonNullValue(eval(json), 'murderer_chance')
        self.cosmetics = checkJsonNullValue(eval(json), 'packages')
        self.hero_wins = checkJsonNullValue(eval(json), 'was_hero')
        self.murderer_kills = checkJsonNullValue(eval(json), 'kills_as_murderer')
        self.murderer_wins = checkJsonNullValue(eval(json), 'murderer_wins')
        self.detective_wins = checkJsonNullValue(eval(json), 'detective_wins')
        self.thrown_knife_kills = checkJsonNullValue(eval(json), 'thrown_knife_kills')
        self.trap_kills = checkJsonNullValue(eval(json), 'trap_kills')
        self.gesture = checkJsonNullValue(eval(json), 'active_gesture')
        self.victory_dance = checkJsonNullValue(eval(json), 'active_victory_dance')
        self.suicides = checkJsonNullValue(eval(json), 'suicides')
        self.projectile_trail = checkJsonNullValue(eval(json), 'active_projectile_trail')
        self.last_words = checkJsonNullValue(eval(json), 'active_last_words')
        self.kill_note = checkJsonNullValue(eval(json), 'active_kill_note')
        self.hat = checkJsonNullValue(eval(json), 'active_animated_hat')
        self.death_cry = checkJsonNullValue(eval(json), 'active_deathcry')
