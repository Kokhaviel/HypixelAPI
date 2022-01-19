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

import os
import time
from error import HypixelAPIException
from pathlib import Path


def get_timestamp_as_millis():
    return int(time.time() * 1000)


def create_cache_if_not_exists():
    cache_dir = str(Path.home()) + "/.hypixel-api/"
    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)
    cache_update = cache_dir + "update.json"

    if not os.path.exists(cache_update):
        file = open(cache_update, 'a')
        file.write("{}")
        file.close()


def clear_one_hour_cache():
    cache_dir = str(Path.home()) + "/.hypixel-api/"
    cache_update = cache_dir + "update.json"
    cache_file = open(cache_update, 'r+')
    cache_update_contents = eval(cache_file.read())

    cache_keys = cache_update_contents.keys()

    for key in cache_keys:
        now = get_timestamp_as_millis()
        if now - int(cache_update_contents[key]) > 3600000:
            try:
                os.remove(cache_dir + "/.hypixel-api/" + key + ".json")
                del cache_update_contents[key]
            except FileNotFoundError:
                raise HypixelAPIException('An error occurred using the cache system')
            finally:
                cache_file.write(str(cache_update_contents))
                cache_file.close()


def invalidate_five_minutes_cache(cache_name):
    cache_dir = str(Path.home()) + "/.hypixel-api/"
    cache_update = cache_dir + "update.json"
    cache_file = open(cache_update, 'r+')
    cache_update_contents = eval(cache_file.read())

    now = get_timestamp_as_millis()

    if not os.path.exists(cache_dir + "/.hypixel-api/" + cache_name + ".json"):
        return

    if now - int(cache_update_contents[cache_name]) > 300000:
        try:
            os.remove(cache_dir + "/.hypixel-api/" + cache_name + ".json")
            del cache_update_contents[cache_name]
        except FileNotFoundError:
            raise HypixelAPIException('An error occurred using the cache system')
        finally:
            cache_file.write(str(cache_update_contents))
            cache_file.close()


def clean_cache():
    cache_dir = str(Path.home()) + "/.hypixel-api/"
    cache_files = os.listdir(cache_dir)

    for file in cache_files:
        if file == 'update.json':
            return
        os.remove(cache_dir + file)

    cache_update = cache_dir + "update.json"
    cache_file = open(cache_update, 'r+')
    cache_update_contents = eval(cache_file.read())

    cache_keys = cache_update_contents.keys()

    for key in cache_keys:
        del cache_update_contents[key]

    cache_file.write(str(cache_update_contents))
    cache_file.close()


def create_cache(cache_name, cache_contents):
    cache_dir = str(Path.home()) + "/.hypixel-api/"
    cache_update = cache_dir + "update.json"
    cache_file = cache_dir + cache_name + ".json"

    cache_file_update = open(cache_update, 'r+')
    cache_update_contents = eval(cache_file_update.read())

    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)
    if not os.path.exists(cache_file):
        open(cache_file, 'a').close()  # Create the file
        cache_file_write = open(cache_file, 'r+')
        cache_file_write.write(str(cache_contents))
        cache_update_contents[cache_name] = get_timestamp_as_millis()
        cache_file_update.seek(0)
        cache_file_update.write(str(cache_update_contents).replace("\'", "\""))
        cache_file_write.close()

    cache_file_update.close()
