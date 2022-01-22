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

import os.path
import requests
import cache
from error import HypixelAPIException
from error import RequestException
from models.friends import Friends
from models.key import APIKey
from models.mojang import Mojang
from models.player import Player
from pathlib import Path

cache_dir = str(Path.home()) + "/.hypixel-api/"


def get_mojang_UUID(player):
    url = "https://api.mojang.com/users/profiles/minecraft/" + player
    request_json = get_no_cache(url)
    return Mojang(request_json)


def fetch(url, file_name):
    request = requests.get(url)
    json = request.text
    if validate_status_code(request):
        cache.create_cache(file_name, json)


def get_no_cache(url):
    request = requests.get(url)
    if validate_status_code(request):
        return request.text


def get_from_cache(file_name):
    file = cache_dir + file_name + ".json"
    return open(file, 'r').read()


def fetch_and_get(url, file_name):
    fetch(url, file_name)
    return get_from_cache(file_name)


class HypixelAPI:
    base_url = "https://api.hypixel.net/"

    def __init__(self, api_key):
        self.api_key = api_key
        cache.create_cache_if_not_exists()
        cache.clear_one_hour_cache()
        if self.api_key == "":
            raise HypixelAPIException("API Key Data : You Must Defined an API Key with __init__")

    def get_API__key_info(self):
        file_name = "key-" + self.api_key
        cache.invalidate_five_minutes_cache(file_name)

        if os.path.exists(cache_dir + file_name + ".json"):
            return APIKey(get_from_cache(file_name))
        else:
            url = "https://api.hypixel.net/key?key=" + self.api_key
            return APIKey(fetch_and_get(url, file_name))

    def get_player(self, player):
        file_name = "player-" + get_mojang_UUID(player).uuid
        cache.invalidate_five_minutes_cache(file_name)

        if os.path.exists(cache_dir + file_name + ".json"):
            return Player(get_from_cache(file_name))
        else:
            url = "https://api.hypixel.net/player?uuid=" + get_mojang_UUID(player).uuid + "&key=" + self.api_key
            return Player(fetch_and_get(url, file_name))

    def get_friends(self, player):
        file_name = "friends-" + get_mojang_UUID(player).uuid
        cache.invalidate_five_minutes_cache(file_name)
        if os.path.exists(cache_dir + file_name + ".json"):
            return Friends(get_from_cache(file_name))
        else:
            url = "https://api.hypixel.net/friends?uuid=" + get_mojang_UUID(player).uuid + "&key=" + self.api_key
            return Friends(fetch_and_get(url, file_name))


def validate_status_code(request):

    if request.status_code == 403:
        raise HypixelAPIException(HypixelAPIException("An error occurred while requestion api.hypixel.net : Forbidden"))
    elif request.status_code == 429:
        raise HypixelAPIException(RequestException("An error occurred while requestion api.hypixel.net : Key Throttle"))
    elif request.status_code == 200:
        return True
    else:
        raise HypixelAPIException("Cannot Reach Endpoint and Fetch Data")
