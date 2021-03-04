""" compilemission.py
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
import config
from model import MissionCompiler


def compile_mission():
    """
    Store the active working data to the data model.
    NOTE: This will not save any data to a file

    :param app: The instance of ESMB
    """
    compiler = None
    if config.active_item.type == "mission":
        compiler = MissionCompiler()
    compiler.run()
    config.gui.item_text_pane.update_pane()
# end compile_mission
