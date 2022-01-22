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

from models.games.arcade import Arcade
from models.games.arena import Arena
from models.games.battleground import BattleGround
from models.games.bedwars import Bedwars
from models.games.build_battle import BuildBattle
from models.games.duels import Duels
from models.games.gingerbread import GingerBread
from models.games.legacy import Legacy
from models.games.mcgo import MCGO
from models.games.megawalls import MegaWalls
from models.games.murdermystery import MurderMystery
from models.games.paintball import Paintball
from models.games.pit import Pit
from models.games.quake import Quake
from models.games.skywars import Skywars
from models.games.smash import Smash
from models.games.speeduhc import SpeedUHC
from models.games.tnt import TNTGames
from models.games.uhc import UHC
from models.games.vampirez import VampireZ
from models.games.walls import Walls

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
