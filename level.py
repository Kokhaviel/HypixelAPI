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

import math


class Level:

    def __init__(self, exp):
        self.exp = exp

    def get_exact_network_level(self):
        level = (math.sqrt(self.exp + 15312.5) - (125 / math.sqrt(2))) / (25 * math.sqrt(2))
        return float("{:.2f}".format(level))

    def get_exp_to_next_level(self):
        next_level = math.floor(self.get_network_level() + 1)
        needed_exp = (math.pow((25 * math.sqrt(2) * next_level + (125 / math.sqrt(2))), 2) - 15312.5)

        return needed_exp - self.exp

    def get_network_level(self):
        return math.floor(self.get_exact_network_level())

    def get_percentage_to_next_level(self):
        exact_level = self.get_exact_network_level()
        level = self.get_network_level()

        percentage = exact_level - level

        return percentage * 100
