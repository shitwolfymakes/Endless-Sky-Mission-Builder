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
from src.model.file_data_parsers import FileItemParser
from src.model import Mission
from src.model.components.conversations import Conversation


class FileMissionItemParser(FileItemParser):
    """Parses a mission item from a file"""
    def __init__(self, lines):
        tokens = shlex.split(lines[0])
        self.mission = Mission(tokens[1])
        self.mission.lines = lines
        self.lines = self.mission.lines

        self.i = None
        self.line = None
        self.enum_lines = enumerate(self.lines)

        self.logMessagePattern = re.compile(r'^ *')
    #end init


    def run(self):
        """
        Run the parsers, checking for tokens
        Reference: https://github.com/endless-sky/endless-sky/blob/49a387d848e88dc734c93b34013af81f873e70c1/source/Mission.cpp#L106-L259
        """
        logging.debug("\t\tParsing %s from file..." % self.mission.name)

        self.strip_ending_whitespace(self.lines)
        for self.i, self.line in self.enum_lines:
            self.line = self.line.rstrip()
            tokens = self.tokenize(self.line)

            # determine which attribute we've got
            if not tokens:
                continue
            if "mission" in tokens[0]:
                continue
            elif "name" in tokens[0]:
                self._parse_name(tokens)
            elif "description" in tokens[0]:
                self._parse_description(tokens)
            elif "blocked" in tokens[0]:
                self._parse_blocked(tokens)
            elif "deadline" in tokens[0]:
                self._parse_deadline(tokens)
            elif "cargo" in tokens[0]:
                self._parse_cargo(tokens)
            elif "passengers" in tokens[0]:
                self._parse_passengers(tokens)
            elif "illegal" in tokens[0]:
                self._parse_illegal(tokens)
            elif "stealth" in tokens[0]:
                self._parse_stealth()
            elif "invisible" in tokens[0]:
                self._parse_invisible()
            elif tokens[0] in ["priority", "minor"]:
                self._parse_priority_level(tokens)
            elif tokens[0] in ["job", "landing", "assisting", "boarding"]:
                self._parse_where_shown(tokens)
            elif "repeat" in tokens[0]:
                self._parse_repeat(tokens)
            elif "clearance" in tokens[0]:
                self._parse_clearance(tokens)
            elif "infiltrating" in tokens[0]:
                self._parse_infiltrating()
            elif "waypoint" in tokens[0]:
                self._parse_waypoint(tokens)
            elif "stopover" in tokens[0]:
                self._parse_stopover(tokens)
            elif "source" in tokens[0]:
                self._parse_source(tokens)
            elif "destination" in tokens[0]:
                self._parse_destination(tokens)
            elif "on" in tokens:
                self._parse_trigger(tokens)
            elif "to" in tokens:
                self._parse_condition()
            else:
                logging.debug("ERROR: No tokens found on line %d: %s" % (self.i, self.line))
            #end if/elif/else
        #end for

        config.mission_file_items.add_item(self.mission)
    #end run


    def _parse_name(self, tokens):
        logging.debug("\t\t\tFound mission display name: \"%s\"" % tokens[1])
        self.mission.components.mission_display_name = tokens[1]
    #end _parse_name


    def _parse_description(self, tokens):
        logging.debug("\t\t\tFound description: %s" % tokens[1])
        self.mission.components.description = tokens[1]
    #end _parse_description


    def _parse_blocked(self, tokens):
        logging.debug("\t\t\tFound blocked: %s" % tokens[1])
        self.mission.components.blocked = tokens[1]
    #end _parse_blocked


    def _parse_deadline(self, tokens):
        logging.debug("\t\t\tFound deadline")
        self.mission.components.deadline.is_active = True
        self.store_component_data(self.mission.components.deadline.deadline, tokens[1:])
    #end _parse_deadline


    def _parse_cargo(self, tokens):
        logging.debug("\t\t\tFound cargo: %s" % tokens[1:])
        self.mission.components.cargo.is_active = True
        self.store_component_data(self.mission.components.cargo.cargo, tokens[1:])
    #end _parse_cargo


    def _parse_passengers(self, tokens):
        logging.debug("\t\t\tFound passengers: %s" % tokens[1:])
        self.mission.components.passengers.is_active = True
        self.store_component_data(self.mission.components.passengers.passengers, tokens[1:])
    #end _parse_passengers


    def _parse_illegal(self, tokens):
        logging.debug("\t\t\tFound illegal modifier: %s" % tokens[1:])
        self.mission.components.illegal.is_active = True
        self.store_component_data(self.mission.components.illegal.illegal, tokens[1:])
    #end _parse_illegal


    def _parse_stealth(self):
        logging.debug("\t\t\tFound stealth modifier")
        self.mission.components.is_stealth = True
    #end _parse_stealth


    def _parse_invisible(self):
        logging.debug("\t\t\tFound invisible modifier")
        self.mission.components.is_invisible = True
    #end _parse_invisible


    def _parse_priority_level(self, tokens):
        logging.debug("\t\t\tFound priority level")
        self.mission.components.priority_level = tokens[0]
    #end _parse_priority_level


    def _parse_where_shown(self, tokens):
        logging.debug("\t\t\tFound where shown")
        self.mission.components.where_shown = tokens[0]
    #end _parse_where_shown


    def _parse_repeat(self, tokens):
        logging.debug("\t\t\tFound repeat")
        self.mission.components.repeat.is_active = True
        if len(tokens) > 1:
            logging.debug("\t\t\t\tFound repeat optional data: %s" % tokens[1])
            self.mission.components.repeat.repeat = tokens[1]
        # end if
    #end _parse_repeat


    def _parse_clearance(self, tokens):
        logging.debug("\t\t\tFound clearance: %s" % tokens[1])
        self.mission.components.clearance.is_active = True
        self.mission.components.clearance.clearance = tokens[1]
    #end _parse_clearance


    def _parse_infiltrating(self):
        logging.debug("\t\t\tFound infiltrating")
        self.mission.components.is_infiltrating = True
    #end _parse_infiltrating


    def _parse_waypoint(self, tokens):
        logging.debug("\t\t\tFound waypoint: %s" % tokens[1])
        self.mission.components.waypoint = tokens[1]
    #end _parse_waypoint


    def _parse_stopover(self, tokens):
        logging.debug("\t\t\tFound stopover: %s" % tokens[1])
        self.mission.components.stopover.is_active = True
        self.mission.components.stopover.stopover = tokens[1]
    #end _parse_stopover


    def _parse_source(self, tokens):
        if len(tokens) == 2:
            logging.debug("\t\t\tFound source: %s" % tokens[1])
            self.mission.components.source.is_active = True
            self.mission.components.source.source = tokens[1]
        else:
            logging.error("COMPLEX SOURCE HANDLING NOT YET IMPLEMENTED")
        # end if/else
    #end _parse_source


    def _parse_destination(self, tokens):
        if len(tokens) == 2:
            logging.debug("\t\t\tFound destination: %s" % tokens[1])
            self.mission.components.destination.is_active = True
            self.mission.components.destination.destination = tokens[1]
        # end if
    #end _parse_destination


    def _parse_trigger(self, tokens):
        logging.debug("\t\t\tFound Trigger: on %s" % tokens[1])
        trigger = self.mission.add_trigger()
        trigger.is_active = True
        trigger.trigger_type = tokens[1]

        cur = self.get_indent_level(self.mission.lines[self.i])
        nxt = self.get_indent_level(self.mission.lines[self.i + 1])
        while True:
            if nxt <= cur:
                break
            self.i, self.line = self.enum_lines.__next__()
            self.line = self.line.rstrip()
            tokens = self.tokenize(self.line)

            if "conversation" in tokens[0]:
                self._parse_conversation(tokens)
            elif "dialog" in tokens[0]:
                self._parse_dialog(trigger, tokens)
            elif "outfit" in tokens[0]:
                self._parse_outfit(trigger, tokens)
            elif "require" in tokens[0]:
                self._parse_require(trigger, tokens)
            elif "payment" in tokens[0]:
                self._parse_payment(trigger, tokens)
            elif "event" in tokens[0]:
                self._parse_event(trigger, tokens)
            elif "fail" in tokens[0]:
                self._parse_fail(trigger, tokens)
            elif "log" in tokens[0] and len(tokens) == 2:
                self._parse_log_type_1(trigger, tokens)
            elif "log" in tokens[0]:
                self._parse_log_type_3(trigger, tokens)
            elif tokens[1] in ["=", "+=", "-="]:
                self._parse_condition_type_0(trigger, tokens)
            elif tokens[1] in ["++", "--"]:
                self._parse_condition_type_1(trigger, tokens)
            elif tokens[0] in ["set", "clear"]:
                self._parse_condition_type_2(trigger, tokens)
            else:
                logging.debug("Trigger component no found: ", self.i, self.line)
            # end if/elif/else

            try:
                nxt = self.get_indent_level(self.mission.lines[self.i + 1])
            except IndexError:
                break
        # end while
        trigger.print_trigger()
    #end _parse_trigger


    def _parse_conversation(self, tokens):
        convo = Conversation()

        if len(tokens) is 2:
            convo.name = tokens[1]

        convo_level = self.get_indent_level(self.line)

        in_convo = True
        while in_convo:
            self.i, self.line = self.enum_lines.__next__()
            self.line = self.line.rstrip()
            convo.lines.append(self.line)

            # check if next line is outside of convo
            try:
                next_line = self.mission.lines[self.i + 1]
                nxt = self.get_indent_level(next_line)
            except IndexError:
                break

            tokens = self.tokenize(next_line)
            if not tokens:
                continue
            if nxt <= convo_level:  # THIS GOES AFTER THE CHECK FOR A NEWLINE BECAUSE THERE ARE NEWLINES AFTER CHOICE
                break
            #if tokens[0] in ["on", "to", "mission", "event", "phrase", "dialog"]:
            #    in_convo = False
        # end while

        self.mission.components.trigger_list[-1].add_convo(convo)
    #end _parse_conversation


    def _parse_dialog(self, trigger, tokens):
        if len(tokens) == 2:
            logging.debug("\t\t\t\tFound Dialog: %s" % tokens[1])
            trigger.dialog = tokens[1]
        else:
            logging.error("COMPLEX DIALOG HANDLING NOT YET IMPLEMENTED")
            cur = self.get_indent_level(self.mission.lines[self.i])
            nxt = self.get_indent_level(self.mission.lines[self.i + 1])
            while True:
                if nxt <= cur:
                    break
                self.i, self.line = self.enum_lines.__next__()

                try:
                    nxt = self.get_indent_level(self.mission.lines[self.i + 1])
                except IndexError:
                    break
            # end while
        # end if/else
    #end _parse_dialog


    def _parse_outfit(self, trigger, tokens):
        logging.debug("\t\t\t\tFound Outfit: %s" % tokens)
        self.store_component_data(trigger.outfit, tokens[1:])
    #end _parse_outfit


    def _parse_require(self, trigger, tokens):
        logging.debug("\t\t\t\tFound Require: %s" % tokens)
        self.store_component_data(trigger.require, tokens[1:])
    #end _parse_require


    def _parse_payment(self, trigger, tokens):
        logging.debug("\t\t\t\tFound Outfit: %s" % tokens)
        trigger.is_payment = True
        self.store_component_data(trigger.payment, tokens[1:])
    #end _parse_payment


    def _parse_event(self, trigger, tokens):
        logging.debug("\t\t\t\tFound Event: %s" % tokens)
        self.store_component_data(trigger.event, tokens[1:])
    #end _parse_event


    @staticmethod
    def _parse_fail(trigger, tokens):
        logging.debug("\t\t\t\tFound Fail: %s" % tokens)
        trigger.is_fail = True
        if len(tokens) == 2:
            trigger.fail = tokens[1]
        else:
            logging.error("COMPLEX FAIL HANDLING NOT YET IMPLEMENTED")
        # end if/else
    #end _parse_fail

    @staticmethod
    def _parse_log_type_1(trigger, tokens):
        logging.debug("\t\t\t\tFound Log: %s" % tokens)
        new_log = trigger.add_log()
        new_log.set(1, tokens[1:])
    #end _parse_log_type_1


    @staticmethod
    def _parse_log_type_3(trigger, tokens):
        logging.debug("\t\t\t\tFound Log: %s" % tokens)
        new_log = trigger.add_log()
        new_log.set(3, tokens[1:])
    #end _parse_log_type_3


    @staticmethod
    def _parse_condition_type_0(trigger, tokens):
        logging.debug("\t\t\t\tFound TriggerCondition: %s" % tokens)
        new_tc = trigger.add_tc()
        new_tc.set(0, tokens)
    #end _parse_condition_type_0


    @staticmethod
    def _parse_condition_type_1(trigger, tokens):
        logging.debug("\t\t\t\tFound TriggerCondition: %s" % tokens)
        new_tc = trigger.add_tc()
        new_tc.set(1, tokens)
    #end _parse_condition_type_1


    @staticmethod
    def _parse_condition_type_2(trigger, tokens):
        logging.debug("\t\t\t\tFound TriggerCondition: %s" % tokens)
        new_tc = trigger.add_tc()
        new_tc.set(2, tokens)
    #end _parse_condition_type_2


    def _parse_condition(self):
        # TODO: Handle these
        cur = self.get_indent_level(self.mission.lines[self.i])
        nxt = self.get_indent_level(self.mission.lines[self.i + 1])
        while True:
            if nxt <= cur:
                break
            self.i, self.line = self.enum_lines.__next__()

            try:
                nxt = self.get_indent_level(self.mission.lines[self.i + 1])
            except IndexError:
                break
        # end while
    #end _parse_condition
#end FileMissionItemParser
