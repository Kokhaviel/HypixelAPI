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

class Games:
    type_name = ""
    db_name = ""
    clean_name = ""
    game_id = 0

    def __init__(self, type_name, db_name, clean_name, game_id):
        self.type_name = type_name
        self.db_name = db_name
        self.clean_name = clean_name
        self.game_id = game_id


QUAKECRAFT = Games("QUAKECRAFT", "Quake", "Quake", 2)
WALLS = Games("WALLS", "Walls", "Walls", 3)
PAINTBALL = Games("PAINTBALL", "Paintball", "Paintball", 4)
SURVIVAL_GAMES = Games("SURVIVAL_GAMES", "HungerGames", "Blitz Survival Games", 5)
TNT_GAMES = Games("TNTGAMES", "TNTGames", "TNT Games", 6)
VAMPIREZ = Games("VAMPIREZ", "VampireZ", "VampireZ", 7)
MEGA_WALLS = Games("WALLS3", "Walls3", "Mega Walls", 13)
ARCADE = Games("ARCADE", "Arcade", "Arcade", 14)
ARENA = Games("ARENA", "Arena", "Arena", 17)
UHC = Games("UHC", "UHC", "UHC Champions", 20)
MCGO = Games("MCGO", "MCGO", "Cops and Crims", 21)
BATTLEGROUND = Games("BATTLEGROUND", "Battleground", "Warlords", 23)
SUPER_SMASH = Games("SUPER_SMASH", "SuperSmash", "Smash Heroes", 24)
GINGERBREAD = Games("GINGERBREAD", "GingerBread", "Turbo Kart Racers", 25)
HOUSING = Games("HOUSING", "Housing", "Housing", 26)
SKYWARS = Games("SKYWARS", "SkyWars", "SkyWars", 51)
TRUE_COMBAT = Games("TRUE_COMBAT", "TrueCombat", "Crazy Walls", 52)
SPEED_UHC = Games("SPEED_UHC", "SpeedUHC", "Speed UHC", 54)
SKYCLASH = Games("SKYCLASH", "SkyClash", "SkyClash", 55)
LEGACY = Games("LEGACY", "Legacy", "Classic Games", 56)
PROTOTYPE = Games("PROTOTYPE", "Prototype", "Prototype", 57)
BEDWARS = Games("BEDWARS", "Bedwars", "Bed Wars", 58)
MURDER_MYSTERY = Games("MURDER_MYSTERY", "MurderMystery", "Murder Mystery", 59)
BUILD_BATTLE = Games("BUILD_BATTLE", "BuildBattle", "Build Battle", 60)
DUELS = Games("DUELS", "Duels", "Duels", 61)
SKYBLOCK = Games("SKYBLOCK", "SkyBlock", "SkyBlock", 63)
PIT = Games("PIT", "Pit", "Pit", 64)
REPLAY = Games("REPLAY", "Replay", "Replay", 65)
SMP = Games("SMP", "SMP", "SMP", 67)
