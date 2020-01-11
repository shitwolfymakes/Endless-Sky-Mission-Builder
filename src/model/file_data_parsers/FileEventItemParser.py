""" FileEventItemParser.py
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
from src.model.events import Event
from src.model.file_data_parsers import FileItemParser


class FileEventItemParser(FileItemParser):
    """Parses an event item from a file"""
    def __init__(self, lines):
        tokens = shlex.split(lines[0])
        self.event = Event(tokens[1])
        self.event.lines = lines
        self.lines = self.event.lines

        self.i = None
        self.line = None
        self.enum_lines = enumerate(self.lines)
    #end init


    def run(self):
        logging.debug("\t\tParsing %s from file..." % self.event.name)

        self.strip_ending_whitespace(self.lines)
        for self.i, self.line in self.enum_lines:
            self.line = self.line.rstrip()
            tokens = self.tokenize(self.line)

            #TODO: Deal with processing this stuff out later
            pass
        #end for

        config.mission_file_items.add_item(self.event)
    #end run
#end class FileEventItemParser
