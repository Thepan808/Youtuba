#!/usr/bin/env python3
# Copyright (C) @subinps
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
class Config:
    API_ID = int(os.environ.get("API_ID", '4954361'))
    API_HASH = os.environ.get("API_HASH", "43a786a8548a30f9d6887e36d53c0e64")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5901798571:AAES32Up_Mbuop_iGaXMaNZqH0fySjhttZA")     
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", '-1001532430686'))
