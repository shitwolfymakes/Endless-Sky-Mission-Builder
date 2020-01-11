""" FileNPCItemParser.py
# Copyright (c) 2020 by Andrew Sneed
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
import shlex

from src import config
from src.model.npcs import NPC
from model.file_data_parsers import FileItemParser


class FileNPCItemParser(FileItemParser):
    """Parses an npc item from a file"""
    def __init__(self, lines):
        tokens = shlex.split(lines[0])
        self.npc = NPC(tokens[1])
        self.npc.lines = lines
        self.lines = self.npc.lines

        self.i = None
        self.line = None
        self.enum_lines = enumerate(self.lines)
    #end init

    def run(self):
        pass
    #end run
#end FileNPCItemParser
