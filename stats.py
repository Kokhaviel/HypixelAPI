#  Copyright (c) 2021 Kokhaviel.
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

from games.arcade import Arcade
from games.arena import Arena
from games.battleground import BattleGround
from games.bedwars import Bedwars
from games.build_battle import BuildBattle
from games.duels import Duels
from games.gingerbread import GingerBread
from games.legacy import Legacy
from games.mcgo import MCGO
from games.megawalls import MegaWalls
from games.murdermystery import MurderMystery
from games.paintball import Paintball
from games.pit import Pit
from games.quake import Quake
from games.skywars import Skywars
from games.smash import Smash
from games.speeduhc import SpeedUHC
from games.tnt import TNTGames
from games.uhc import UHC
from games.vampirez import VampireZ
from games.walls import Walls

from utils import checkJsonNullValue


class Stats:

    def __init__(self, json):
        self.arcade = Arcade(checkJsonNullValue(eval(json), 'Arcade'))
        self.arena = Arena(checkJsonNullValue(eval(json), 'Arena'))
        self.battleground = BattleGround(checkJsonNullValue(eval(json), 'Battleground'))
        self.bedwars = Bedwars(checkJsonNullValue(eval(json), 'Bedwars'))
        self.build_battle = BuildBattle(checkJsonNullValue(eval(json), 'BuildBattle'))
        self.duels = Duels(checkJsonNullValue(eval(json), 'Duels'))
        self.gingerbread = GingerBread(checkJsonNullValue(eval(json), 'GingerBread'))
        self.legacy = Legacy(checkJsonNullValue(eval(json), 'Legacy'))
        self.mcgo = MCGO(checkJsonNullValue(eval(json), 'MCGO'))
        self.mega_walls = MegaWalls(checkJsonNullValue(eval(json), 'Walls3'))
        self.murder_mystery = MurderMystery(checkJsonNullValue(eval(json), 'MurderMystery'))
        self.paintball = Paintball(checkJsonNullValue(eval(json), 'Paintball'))
        self.pit = Pit(checkJsonNullValue(eval(json), 'Pit'))
        self.quake = Quake(checkJsonNullValue(eval(json), 'Quake'))
        self.skywars = Skywars(checkJsonNullValue(eval(json), 'SkyWars'))
        self.smash = Smash(checkJsonNullValue(eval(json), 'SuperSmash'))
        self.speed_uhc = SpeedUHC(checkJsonNullValue(eval(json), 'SpeedUHC'))
        self.tnt_games = TNTGames(checkJsonNullValue(eval(json), 'TNTGames'))
        self.uhc = UHC(checkJsonNullValue(eval(json), 'UHC'))
        self.vampirez = VampireZ(checkJsonNullValue(eval(json), 'VampireZ'))
        self.walls = Walls(checkJsonNullValue(eval(json), 'Walls'))
