""" MissionFileParser.py
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

#TODO: Add data validation, there are currently no checks to make sure it's not all junk data
import re
import logging

import src.model.file_data_parsers as parsers


class MissionFileParser:
    """This takes the data read in from a mission file and stores it in each mission object"""
    def __init__(self, mission_lines):
        self.lines = mission_lines
        self.file_items = []

        self.match_mission = re.compile(r'^ *mission')
        self.match_event = re.compile(r'^event')
        self.match_phrase = re.compile(r'^phrase')
        self.match_npc = re.compile(r'^npc')
        self.match_government = re.compile(r'^government')
    #end init

    def run(self):
        """Runs the parser"""
        logging.debug("\tParsing Mission file...")

        #TODO: break this into multiple functions
        enum_lines = enumerate(self.lines)
        for i, line in enum_lines:
            line.rstrip()
            if line == "" or line == "\n":
                continue

            line = line.rstrip("\n")
            if re.search(self.match_mission, line):
                logging.debug("\t\tMISSION FOUND: %s" % line)
                self.store_item_for_parsing(i, line, "mission")
            elif re.search(self.match_event, line):
                logging.debug("\t\tEVENT FOUND: %s" % line)
                self.store_unhandled_items_for_parsing(i, line, "event")
            elif re.search(self.match_phrase, line):
                logging.debug("\t\tPHRASE FOUND: %s" % line)
                self.store_unhandled_items_for_parsing(i, line, "phrase")
            elif re.search(self.match_npc, line):
                logging.debug("\t\tNPC FOUND: %s" % line)
                self.store_unhandled_items_for_parsing(i, line, "npc")
            elif re.search(self.match_government, line):
                logging.debug("\t\tGOVERNMENT FOUND: %s" % line)
                self.store_unhandled_items_for_parsing(i, line, "government")
            #end elif
        #end for

        for item in self.file_items:
            if item[0] is "mission":
                parser = parsers.FileMissionItemParser(item[1])
                parser.run()
            elif item[0] is "event":
                parser = parsers.FileEventItemParser(item[1])
                parser.run()
            elif item[0] is "phrase":
                pass
            elif item[0] is "npc":
                pass
            elif item[0] is "government":
                pass
            #end if/else
        #end for

        logging.debug("File parsing complete.")
    #end run


    def store_item_for_parsing(self, i, line, item_type):
        item_lines = [line + "\n"]
        lines = self.lines[i+1:]
        for i, line in enumerate(lines):
            if self.end_of_item_condition(line):
                self.file_items.append((item_type, item_lines))
                break
            #end if

            item_lines.append(line)
            if self.is_eof(i, lines):
                self.file_items.append((item_type, item_lines))
                break
            #end if
        #end for
    #end store_item_for_parsing


    def store_unhandled_items_for_parsing(self, i, line, item_type):
        item_lines = [line]
        lines = self.lines[i+1:]
        for i, line in enumerate(lines):
            if self.end_of_item_condition(line) or self.is_eof(i, lines):
                self.file_items.append((item_type, item_lines))
                break
            #end if
            item_lines.append(line)
        #end for
    #end store_item_for_parsing


    def end_of_item_condition(self, line):
        is_end = False

        if re.match(self.match_mission, line):
            is_end = True
        elif re.match(self.match_event, line):
            is_end = True
        elif re.match(self.match_phrase, line):
            is_end = True
        elif re.match(self.match_npc, line):
            is_end = True
        elif re.match(self.match_government, line):
            is_end = True
        #end if/else

        return is_end
    #end end_of_item_condition


    @staticmethod
    def is_eof(i, lines):
        try:
            if lines[i+1]:
                return False
        except IndexError:
            return True
    #end not_EOF
#end class MissionFileParser
