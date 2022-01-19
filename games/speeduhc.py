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


class SpeedUHC:

    def __init__(self, json):
        self.cosmetics = checkJsonNullValue(eval(json), 'packages')
        self.tear_well_uses = checkJsonNullValue(eval(json), 'tearWellUses')
        self.tears = checkJsonNullValue(eval(json), 'tears')
        self.killstreak = checkJsonNullValue(eval(json), 'killstreak')
        self.best_killstreak = checkJsonNullValue(eval(json), 'highestKillstreak')
        self.winstreak = checkJsonNullValue(eval(json), 'winstreak')
        self.coins = checkJsonNullValue(eval(json), 'coins')
        self.losses = checkJsonNullValue(eval(json), 'losses')
        self.quits = checkJsonNullValue(eval(json), 'quits')
        self.kills = checkJsonNullValue(eval(json), 'kills')
        self.deaths = checkJsonNullValue(eval(json), 'deaths')
        self.survived_players = checkJsonNullValue(eval(json), 'survived_players')
        self.assists = checkJsonNullValue(eval(json), 'assists')
        self.blocks_placed = checkJsonNullValue(eval(json), 'blocks_placed')
        self.items_enchanted = checkJsonNullValue(eval(json), 'items_enchanted')
        self.games_played = checkJsonNullValue(eval(json), 'games')
        self.wins = checkJsonNullValue(eval(json), 'wins')
        self.arrows_shot = checkJsonNullValue(eval(json), 'arrows_shot')
        self.arrows_hit = checkJsonNullValue(eval(json), 'arrows_hit')
        self.score = checkJsonNullValue(eval(json), 'score')
        self.victory_dance = checkJsonNullValue(eval(json), 'active_victorydance')
        self.kill_effect = checkJsonNullValue(eval(json), 'active_killeffect')
        self.cage = checkJsonNullValue(eval(json), 'active_cage')
        self.projectile_trail = checkJsonNullValue(eval(json), 'active_projectiletrail')
