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
from level import Level
from utils import checkJsonNullValue
from models.stats import Stats


class Player:

    def __init__(self, json):

        true = True
        false = False

        self.success = checkJsonNullValue(eval(json), 'success')

        player = checkJsonNullValue(eval(json), 'player')

        vanity_meta = checkJsonNullValue(eval(player), 'vanityMeta')
        housing_meta = checkJsonNullValue(eval(player), 'housingMeta')
        challenges = checkJsonNullValue(eval(player), 'challenges')

        self.id = checkJsonNullValue(eval(player), '_id')
        self.uuid = checkJsonNullValue(eval(player), 'uuid')
        self.first_login = checkJsonNullValue(eval(player), 'firstLogin')
        self.player_name = checkJsonNullValue(eval(player), 'playername')
        self.last_login = checkJsonNullValue(eval(player), 'lastLogin')
        self.display_name = checkJsonNullValue(eval(player), 'displayname')
        self.aliases = checkJsonNullValue(eval(player), 'knownAliases')
        self.aliases_lower = checkJsonNullValue(eval(player), 'knownAliasesLower')
        self.achievements_one_time = checkJsonNullValue(eval(player), 'achievementsOneTime')
        self.achievements_points = checkJsonNullValue(eval(player), 'achievementPoints')
        self.quickjoin_uses = checkJsonNullValue(eval(player), 'quickjoin_uses')
        self.network_exp = checkJsonNullValue(eval(player), 'networkExp')
        self.last_logout = checkJsonNullValue(eval(player), 'lastLogout')
        self.pet_consumables = checkJsonNullValue(eval(player), 'petConsumables')
        self.spec_first_person = checkJsonNullValue(eval(player), 'spec_first_person')
        self.karma = checkJsonNullValue(eval(player), 'karma')
        self.friend_requests_uuid = checkJsonNullValue(eval(player), 'friendRequestsUuid')
        self.mc_version_rp = checkJsonNullValue(eval(player), 'mcVersionRp')
        self.user_language = checkJsonNullValue(eval(player), 'userLanguage')
        self.vanity_favorites = checkJsonNullValue(eval(player), 'vanityFavorites')
        self.adsense_tokens = checkJsonNullValue(eval(player), 'adsense_tokens')
        self.rank = checkJsonNullValue(eval(player), 'rank', 'PLAYER')
        self.new_package_rank = checkJsonNullValue(eval(player), 'newPackageRank', 'NONE')
        self.rank_plus_color = checkJsonNullValue(eval(player), 'rankPlusColor', 'NONE')
        self.last_claimed_reward = checkJsonNullValue(eval(player), 'lastClaimedReward')
        self.reward_high_score = checkJsonNullValue(eval(player), 'rewardHighScore')
        self.reward_score = checkJsonNullValue(eval(player), 'rewardScore')
        self.reward_streak = checkJsonNullValue(eval(player), 'rewardStreak')
        self.total_daily_rewards = checkJsonNullValue(eval(player), 'totalDailyRewards')
        self.total_rewards = checkJsonNullValue(eval(player), 'totalRewards')
        self.current_gadget = checkJsonNullValue(eval(player), 'currentGadget')
        self.current_cloak = checkJsonNullValue(eval(player), 'currentCloak')
        self.current_pet = checkJsonNullValue(eval(player), 'currentPet', 'NONE')
        self.most_recent_game_type = checkJsonNullValue(eval(player), 'mostRecentGameType')
        self.achievements = checkJsonNullValue(eval(player), 'achievements')
        self.medias = Medias(checkJsonNullValue(eval(player), 'socialMedia'))
        self.stats = Stats(checkJsonNullValue(eval(player), 'stats'))

        self.hub_cosmetics = checkJsonNullValue(eval(vanity_meta), 'packages')
        self.housing_blocks = checkJsonNullValue(eval(housing_meta), 'allowedBlocks')
        self.housing_cosmetics = checkJsonNullValue(eval(housing_meta), 'packages')
        self.challenges = checkJsonNullValue(eval(challenges), 'all_time')

        self.outfit = Outfit(checkJsonNullValue(eval(player), 'outfit'))

        def get_level():
            return Level(self.network_exp)


class Outfit:

    def __init__(self, json):
        self.helmet = checkJsonNullValue(eval(json), 'HELMET')
        self.chestplate = checkJsonNullValue(eval(json), 'CHESTPLATE')
        self.leggings = checkJsonNullValue(eval(json), 'LEGGINGS')
        self.boots = checkJsonNullValue(eval(json), 'BOOTS')


class Medias:

    def __init__(self, json):
        links = checkJsonNullValue(eval(json), 'links')

        self.twitter = checkJsonNullValue(eval(links), 'TWITTER')
        self.youtube = checkJsonNullValue(eval(links), 'YOUTUBE')
        self.instagram = checkJsonNullValue(eval(links), 'INSTAGRAM')
        self.twitch = checkJsonNullValue(eval(links), 'TWITCH')
        self.discord = checkJsonNullValue(eval(links), "DISCORD")
        self.hypixel_forums = checkJsonNullValue(eval(links), "HYPIXEL")
