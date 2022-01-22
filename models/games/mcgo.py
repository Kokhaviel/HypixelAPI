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


class MCGO:

    def __init__(self, json):
        self.bombs_defused = checkJsonNullValue(eval(json), 'bombs_defused')
        self.bombs_planted = checkJsonNullValue(eval(json), 'bombs_planted')
        self.coins = checkJsonNullValue(eval(json), 'coins')
        self.cop_kills = checkJsonNullValue(eval(json), 'cop_kills')
        self.criminal_kills = checkJsonNullValue(eval(json), 'criminal_kills')
        self.deaths = checkJsonNullValue(eval(json), 'deaths')
        self.wins = checkJsonNullValue(eval(json), 'game_wins')
        self.headshots = checkJsonNullValue(eval(json), 'headshot_kills')
        self.kills = checkJsonNullValue(eval(json), 'kills')
        self.shots_fired = checkJsonNullValue(eval(json), 'shots_fired')
        self.cosmetics = checkJsonNullValue(eval(json), 'packages')
        self.lobby_prefix = checkJsonNullValue(eval(json), 'selected_lobby_prefix')
        self.grenade_kills = checkJsonNullValue(eval(json), 'grenade_kills')
        self.pistol_kills = checkJsonNullValue(eval(json), 'pistolKills')
        self.carbine_kills = checkJsonNullValue(eval(json), 'carbineKills')
        self.assists = checkJsonNullValue(eval(json), 'assists')
        self.rifle_kills = checkJsonNullValue(eval(json), 'rifleKills')
        self.sniper_kills = checkJsonNullValue(eval(json), 'sniperKills')
