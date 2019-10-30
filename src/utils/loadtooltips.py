""" loadtooltips.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
"""

import logging
import json
import os
import sys


def load_tooltips():
    logging.debug("\tLoading tooltips...")
    file_path = os.path.join(sys.path[0], "data", "tooltips.json")
    with open(file_path) as data_file:
        logging.debug("\tTooltips JSON file opened...")
        data = json.load(data_file)
    #end with open
    return data
#end load_tooltips
