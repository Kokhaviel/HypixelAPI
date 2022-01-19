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


class BuildBattle:

    def __init__(self, json):
        self.cosmetics = checkJsonNullValue(eval(json), 'packages')
        self.wins_solo_normal = checkJsonNullValue(eval(json), 'wins_solo_normal')
        self.wins = checkJsonNullValue(eval(json), 'wins')
        self.games_played = checkJsonNullValue(eval(json), 'games_played')
        self.score = checkJsonNullValue(eval(json), 'score')
        self.coins = checkJsonNullValue(eval(json), 'coins')
        self.total_votes = checkJsonNullValue(eval(json), 'total_votes')
        self.music = checkJsonNullValue(eval(json), 'music')
        self.wins_teams_normal = checkJsonNullValue(eval(json), 'wins_teams_normal')
        self.wins_solo_pro = checkJsonNullValue(eval(json), 'wins_solo_pro')
        self.correct_guesses = checkJsonNullValue(eval(json), 'correct_guesses')
        self.super_votes = checkJsonNullValue(eval(json), 'super_votes')
        self.wins_guess_the_build = checkJsonNullValue(eval(json), 'wins_guess_the_build')
        self.last_song = checkJsonNullValue(eval(json), 'last_purchased_song')
        self.backdrop = checkJsonNullValue(eval(json), 'selected_backdrop')
        self.victory_dance = checkJsonNullValue(eval(json), 'new_victory_dance')
        self.hat = checkJsonNullValue(eval(json), 'new_selected_hat')
        self.trail = checkJsonNullValue(eval(json), 'active_movement_trail')
