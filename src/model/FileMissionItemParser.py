""" FileMissionItemParser.py
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
import re
import shlex

from src import config
from src.model import Mission
from src.model.components.conversations import Conversation


class FileMissionItemParser:
    """Parses a mission item from a file"""
    def __init__(self, lines):
        tokens = shlex.split(lines[0])
        self.mission = Mission(tokens[1])
        self.mission.lines = lines
        self.lines = self.mission.lines

        self.logMessagePattern = re.compile(r'^ *')
    #end init


    def run(self):
        print("Parsing %s from file..." % self.mission.name)

        self.strip_ending_whitespace_from_lines()
        enum_lines = enumerate(self.lines)
        for i, line in enum_lines:
            line = line.rstrip()
            tokens = self.tokenize(line)

            # determine which attribute we've got
            if not tokens:
                continue
            if "mission" in tokens[0]:
                continue
            elif "name" in tokens[0]:
                logging.debug("\t\tFound mission display name: \"%s\"" % tokens[1])
                self.mission.components.mission_display_name = tokens[1]
            elif "description" in tokens[0]:
                logging.debug("\t\tFound description: %s" % tokens[1])
                self.mission.components.description = tokens[1]
            elif "blocked" in tokens[0]:
                logging.debug("\t\tFound blocked: %s" % tokens[1])
                self.mission.components.blocked = tokens[1]
            elif "deadline" in tokens[0]:
                logging.debug("\t\tFound deadline")
                self.mission.components.deadline.is_active = True
                self.store_component_data(self.mission.components.deadline.deadline, tokens[1:])
            elif "cargo" in tokens[0]:
                logging.debug("\t\tFound cargo: %s" % tokens[1:])
                self.mission.components.cargo.is_active = True
                self.store_component_data(self.mission.components.cargo.cargo, tokens[1:])
            elif "passengers" in tokens[0]:
                logging.debug("\t\tFound passengers: %s" % tokens[1:])
                self.mission.components.passengers.is_active = True
                self.store_component_data(self.mission.components.passengers.passengers, tokens[1:])
            elif "illegal" in tokens[0]:
                logging.debug("\t\tFound illegal modifier: %s" % tokens[1:])
                self.mission.components.illegal.is_active = True
                self.store_component_data(self.mission.components.illegal.illegal, tokens[1:])
            elif "stealth" in tokens[0]:
                logging.debug("\t\tFound stealth modifier")
                self.mission.components.is_stealth = True
            elif "invisible" in tokens[0]:
                logging.debug("\t\tFound invisible modifier")
                self.mission.components.is_invisible = True
            elif tokens[0] in ["priority", "minor"]:
                logging.debug("\t\tFound priority level")
                self.mission.components.priority_level = tokens[0]
            elif tokens[0] in ["job", "landing", "assisting", "boarding"]:
                logging.debug("\t\tFound where shown")
                self.mission.components.where_shown = tokens[0]
            elif "repeat" in tokens[0]:
                logging.debug("\t\tFound repeat")
                self.mission.components.repeat.is_active = True
                if len(tokens) > 1:
                    logging.debug("\t\t\tFound repeat optional data: %s" % tokens[1])
                    self.mission.components.repeat.repeat = tokens[1]
            elif "clearance" in tokens[0]:
                logging.debug("\t\tFound clearance: %s" % tokens[1])
                self.mission.components.clearance.is_active = True
                self.mission.components.clearance.clearance   = tokens[1]
            elif "infiltrating" in tokens[0]:
                logging.debug("\t\tFound infiltrating")
                self.mission.components.is_infiltrating = True
            elif "waypoint" in tokens[0]:
                logging.debug("\t\tFound waypoint: %s" % tokens[1])
                self.mission.components.waypoint = tokens[1]
            elif "stopover" in tokens[0]:
                logging.debug("\t\tFound stopover: %s" % tokens[1])
                self.mission.components.stopover.is_active = True
                self.mission.components.stopover.stopover   = tokens[1]
            elif "source" in tokens[0]:
                if len(tokens) == 2:
                    logging.debug("\t\tFound source: %s" % tokens[1])
                    self.mission.components.source.is_active = True
                    self.mission.components.source.source   = tokens[1]
                else:
                    logging.error("COMPLEX SOURCE HANDLING NOT YET IMPLEMENTED")
            elif "destination" in tokens[0]:
                if len(tokens) == 2:
                    logging.debug("\t\tFound destination: %s" % tokens[1])
                    self.mission.components.destination.is_active = True
                    self.mission.components.destination.destination = tokens[1]
            elif "on" in tokens:
                logging.debug("\t\tFound Trigger: on %s" % tokens[1])
                trigger = self.mission.add_trigger()
                trigger.is_active = True
                trigger.trigger_type = tokens[1]

                cur = self.get_indent_level(self.mission.lines[i])
                nxt = self.get_indent_level(self.mission.lines[i+1])
                while True:
                    if nxt <= cur:
                        break
                    i, line = enum_lines.__next__()
                    line = line.rstrip()
                    tokens = self.tokenize(line)

                    if "conversation" in tokens[0]:
                        #TODO: Store the conversation in the trigger
                        convo = Conversation()
                        if len(tokens) is 2:
                            convo.name = tokens[1]
                        in_convo = True
                        while in_convo:
                            i, line = enum_lines.__next__()
                            line = line.rstrip()
                            tokens = self.tokenize(line)
                            convo.lines.append(line)

                            # check if next line is outside of convo
                            try:
                                next_line = self.mission.lines[i+1]
                            except IndexError:
                                break

                            tokens = self.tokenize(next_line)
                            if not tokens:
                                continue
                            if tokens[0] in ["on", "to", "mission", "event", "phrase"]:
                                in_convo = False
                        # end while
                    elif "dialog" in tokens[0]:
                        if len(tokens) == 2:
                            logging.debug("\t\t\tFound Dialog: %s" % tokens[1])
                            trigger.dialog = tokens[1]
                        else:
                            logging.error("COMPLEX DIALOG HANDLING NOT YET IMPLEMENTED")
                            cur = self.get_indent_level(self.mission.lines[i])
                            nxt = self.get_indent_level(self.mission.lines[i + 1])
                            while True:
                                if nxt <= cur:
                                    break
                                i, line = enum_lines.__next__()

                                try:
                                    nxt = self.get_indent_level(self.mission.lines[i + 1])
                                except IndexError:
                                    break
                            # end while
                    elif "outfit" in tokens[0]:
                        logging.debug("\t\t\tFound Outfit: %s" % tokens)
                        self.store_component_data(trigger.outfit, tokens[1:])
                    elif "require" in tokens[0]:
                        logging.debug("\t\t\tFound Require: %s" % tokens)
                        self.store_component_data(trigger.require, tokens[1:])
                    elif "payment" in tokens[0]:
                        logging.debug("\t\t\tFound Outfit: %s" % tokens)
                        trigger.is_payment = True
                        self.store_component_data(trigger.payment, tokens[1:])
                    elif "event" in tokens[0]:
                        logging.debug("\t\t\tFound Event: %s" % tokens)
                        self.store_component_data(trigger.event, tokens[1:])
                    elif "fail" in tokens[0]:
                        logging.debug("\t\t\tFound Fail: %s" % tokens)
                        trigger.is_fail = True
                        if len(tokens) == 2:
                            trigger.fail = tokens[1]
                        else:
                            logging.error("COMPLEX FAIL HANDLING NOT YET IMPLEMENTED")
                    elif "log" in tokens[0] and len(tokens) == 2:
                        logging.debug("\t\t\tFound Log: %s" % tokens)
                        new_log             = trigger.add_log()
                        new_log.is_active   = True
                        new_log.format_type = "<message>"
                        new_log.log[0]      = tokens[1]
                    elif "log" in tokens[0]:
                        logging.debug("\t\t\tFound Log: %s" % tokens)
                        new_log             = trigger.add_log()
                        new_log.is_active   = True
                        new_log.format_type = "<type> <name> <message>"
                        self.store_component_data(new_log.log, tokens[1:])
                    elif tokens[1] in ["=", "+=", "-="]:
                        logging.debug("\t\t\tFound TriggerCondition: %s" % tokens)
                        new_tc                = trigger.add_tc()
                        new_tc.is_active      = True
                        new_tc.condition_type = 0
                        self.store_component_data(new_tc.condition, tokens)
                    elif tokens[1] in ["++", "--"]:
                        logging.debug("\t\t\tFound TriggerCondition: %s" % tokens)
                        new_tc                = trigger.add_tc()
                        new_tc.is_active      = True
                        new_tc.condition_type = 1
                        self.store_component_data(new_tc.condition, tokens)
                    elif tokens[0] in ["set", "clear"]:
                        logging.debug("\t\t\tFound TriggerCondition: %s" % tokens)
                        new_tc                = trigger.add_tc()
                        new_tc.is_active      = True
                        new_tc.condition_type = 2
                        self.store_component_data(new_tc.condition, tokens)
                    else:
                        logging.debug("Trigger component no found: ", i, line)
                    #end if/elif/else

                    try:
                        nxt = self.get_indent_level(self.mission.lines[i+1])
                    except IndexError:
                        break
                #end while
            elif "to" in tokens:
                #TODO: Handle these
                cur = self.get_indent_level(self.mission.lines[i])
                nxt = self.get_indent_level(self.mission.lines[i+1])
                while True:
                    if nxt <= cur:
                        break
                    i, line = enum_lines.__next__()

                    try:
                        nxt = self.get_indent_level(self.mission.lines[i+1])
                    except IndexError:
                        break
                # end while
            else:
                logging.debug("ERROR: No tokens found on line %d: %s" % (i, line))
            #end if/else
            for trigger in self.mission.components.trigger_list:
                trigger.print_trigger()
            #end for
        #end for

        config.mission_file_items.add_item(self.mission)
        self.mission.print_item_lines_to_text()
    #end run


    def strip_ending_whitespace_from_lines(self):
        while self.lines[-1] == "" or self.lines[-1] == "\n":
            del self.lines[-1]
    #end strip_ending_whitespace_from_lines


    @staticmethod
    def tokenize(line):
        """
        Break the line into a list of tokens, saving anything inside quotes as a single token

        :param line: the String to be tokenized
        """
        pattern = re.compile(r'((?:".*?")|(?:`.*?`)|[^\"\s]+)')
        tokens = re.findall(pattern, line)
        for i, token in enumerate(tokens):
            if token.startswith("`"):
                tokens[i] = token[1:-1]
            elif token.startswith("\""):
                tokens[i] = token[1:-1]
        return tokens
    # end tokenize


    @staticmethod
    def get_indent_level(line):
        tab_count = len(line) - len(line.lstrip('\t'))
        return tab_count
    # end get_indent_level


    @staticmethod
    def store_component_data(component, tokens):
        """
        Store the tokens in the given component

        :param component: The component the data will be stored in
        :param tokens: The tokens to store
        """
        for i, token in enumerate(tokens):
            if token is not None:
                component[i] = token
            else:
                break
            # end if/else
        # end for
    # end store_component_data
#end FileMissionItemParser
