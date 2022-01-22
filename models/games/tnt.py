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


class TNTGames:

    def __init__(self, json):
        self.coins = checkJsonNullValue(eval(json), 'coins')
        self.spleef_deaths = checkJsonNullValue(eval(json), 'deaths_bowspleef')
        self.capture_deaths = checkJsonNullValue(eval(json), 'deaths_capture')
        self.double_jump_tnt_run = checkJsonNullValue(eval(json), 'doublejump_tntrun')
        self.capture_kills = checkJsonNullValue(eval(json), 'kills_capture')
        self.cosmetics = checkJsonNullValue(eval(json), 'packages')
        self.double_jump_spleef = checkJsonNullValue(eval(json), 'spleef_doublejump')
        self.spleef_repulse = checkJsonNullValue(eval(json), 'spleef_repulse')
        self.spleef_triple_shot = checkJsonNullValue(eval(json), 'spleef_triple')
        self.spleef_tags = checkJsonNullValue(eval(json), 'tags_bowspleef')
        self.spleef_wins = checkJsonNullValue(eval(json), 'wins_bowspleef')
        self.capture_wins = checkJsonNullValue(eval(json), 'wins_capture')
        self.tnt_tag_wins = checkJsonNullValue(eval(json), 'wins_tntag')
        self.tnt_run_tags = checkJsonNullValue(eval(json), 'wins_tntrun')
        self.capture_class = checkJsonNullValue(eval(json), 'capture_class')
        self.tnt_tag_kills = checkJsonNullValue(eval(json), 'kills_tntag')
        self.capture_assists = checkJsonNullValue(eval(json), 'assists_capture')
        self.tnt_run_record = checkJsonNullValue(eval(json), 'record_tntrun')
        self.tnt_tag_speed = checkJsonNullValue(eval(json), 'tag_speed')
        self.pvp_run_record = checkJsonNullValue(eval(json), 'record_pvprun')
        self.pvp_run_wins = checkJsonNullValue(eval(json), 'wins_pvprun')
        self.pvp_run_kills = checkJsonNullValue(eval(json), 'kills_pvprun')
        self.particle_effect = checkJsonNullValue(eval(json), 'active_particle_effect')
        self.death_effect = checkJsonNullValue(eval(json), 'active_death_effect')
        self.winstreak = checkJsonNullValue(eval(json), 'winstreak')
        self.tnt_tag_blast_protection = checkJsonNullValue(eval(json), 'tag_blastprotection')
        self.tnt_tag_slow_it_down = checkJsonNullValue(eval(json), 'tag_slowitdown')
        self.tnt_tag_speed_it_up = checkJsonNullValue(eval(json), 'tag_speeditup')
        self.tnt_run_speed_potions = checkJsonNullValue(eval(json), 'new_tntrun_speed_potions')
        self.tnt_run_slowness_potions = checkJsonNullValue(eval(json), 'new_tntrun_slowness_potions')
        self.tnt_run_potions_splashed = checkJsonNullValue(eval(json), 'run_potions_splashed_on_players')
        self.pvp_run_notoriety = checkJsonNullValue(eval(json), 'new_pvprun_notoriety')
        self.pvp_run_fortitude = checkJsonNullValue(eval(json), 'new_pvprun_fortitude')
        self.pvp_run_regenration = checkJsonNullValue(eval(json), 'new_pvprun_regeneration')
        self.pvp_run_deaths = checkJsonNullValue(eval(json), 'deaths_pvprun')
        self.tnt_run_deaths = checkJsonNullValue(eval(json), 'deaths_tntrun')
        self.wizards_class = checkJsonNullValue(eval(json), 'wizards_selected_class')
        self.wins = checkJsonNullValue(eval(json), 'wins')
        self.capture_points = checkJsonNullValue(eval(json), 'points_capture')
        self.spleef_arrow_rain = checkJsonNullValue(eval(json), 'new_spleef_arrowrain')
        self.spleef_explosive_dash = checkJsonNullValue(eval(json), 'new_spleef_exlosive_dash')
        self.capture_air_time = checkJsonNullValue(eval(json), 'air_time_capture')
