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


class MissionFileParser(object):
    """This takes the data read in from a mission file and stores it in each mission object"""
    def __init__(self, esmb):
        self.esmb     = esmb
        self.missions = esmb.missionList

        self.logMessagePattern = re.compile(r'^ *')
    #end init

    def run(self):
        """Runs the parser"""
        logging.debug("\tParsing Mission file...")

        for mission in self.missions:
            logging.debug("\tParsing mission: \"%s\"" % mission.missionName)
            lines = enumerate(mission.missionLines)
            for i, line in lines:
                line = line.rstrip()
                tokens = self.tokenize(line)

                # determine which attribute we've got
                if "mission" in tokens[0]:
                    continue
                elif "name" in tokens[0]:
                    logging.debug("\t\tFound mission display name: \"%s\"" % tokens[1])
                    mission.components.missionDisplayName = tokens[1]
                elif "description" in tokens[0]:
                    logging.debug("\t\tFound description: %s" % tokens[1])
                    mission.components.description = tokens[1]
                elif "blocked" in tokens[0]:
                    logging.debug("\t\tFound blocked: %s" % tokens[1])
                    mission.components.blocked = tokens[1]
                elif "deadline" in tokens[0]:
                    logging.debug("\t\tFound deadline")
                    mission.components.deadline.isActive = True
                    self.store_component_data(mission.components.deadline.deadline, tokens[1:])
                elif "cargo" in tokens[0]:
                    logging.debug("\t\tFound cargo: %s" % tokens[1:])
                    mission.components.cargo.isActive = True
                    self.store_component_data(mission.components.cargo.cargo, tokens[1:])
                elif "passengers" in tokens[0]:
                    logging.debug("\t\tFound passengers: %s" % tokens[1:])
                    mission.components.passengers.isActive = True
                    self.store_component_data(mission.components.passengers.passengers, tokens[1:])
                elif "illegal" in tokens[0]:
                    logging.debug("\t\tFound illegal modifier: %s" % tokens[1:])
                    mission.components.illegal.isActive = True
                    self.store_component_data(mission.components.illegal.illegal, tokens[1:])
                elif "stealth" in tokens[0]:
                    logging.debug("\t\tFound stealth modifier")
                    mission.components.isStealth = True
                elif "invisible" in tokens[0]:
                    logging.debug("\t\tFound invisible modifier")
                    mission.components.isInvisible = True
                elif tokens[0] in ["priority", "minor"]:
                    logging.debug("\t\tFound priority level")
                    mission.components.priorityLevel = tokens[0]
                elif tokens[0] in ["job", "landing", "assisting", "boarding"]:
                    logging.debug("\t\tFound where shown")
                    mission.components.whereShown = tokens[0]
                elif "repeat" in tokens[0]:
                    logging.debug("\t\tFound repeat")
                    mission.components.repeat.isActive = True
                    if len(tokens) > 1:
                        logging.debug("\t\t\tFound repeat optional data: %s" % tokens[1])
                        mission.components.repeat.repeat = tokens[1]
                elif "clearance" in tokens[0]:
                    logging.debug("\t\tFound clearance: %s" % tokens[1])
                    mission.components.clearance.isActive = True
                    mission.components.clearance.clearance   = tokens[1]
                elif "infiltrating" in tokens[0]:
                    logging.debug("\t\tFound infiltrating")
                    mission.components.isInfiltrating = True
                elif "waypoint" in tokens[0]:
                    logging.debug("\t\tFound waypoint: %s" % tokens[1])
                    mission.components.waypoint = tokens[1]
                elif "stopover" in tokens[0]:
                    logging.debug("\t\tFound stopover: %s" % tokens[1])
                    mission.components.stopover.isActive = True
                    mission.components.stopover.stopover   = tokens[1]
                elif "source" in tokens[0]:
                    logging.debug("\t\tFound source: %s" % tokens[1])
                    mission.components.source.isActive = True
                    mission.components.source.source   = tokens[1]
                elif "destination" in tokens[0]:
                    logging.debug("\t\tFound destination: %s" % tokens[1])
                    mission.components.destination.isActive = True
                    mission.components.destination.destination   = tokens[1]
                elif "on" in tokens:
                    logging.debug("\t\tFound Trigger: on %s" % tokens[1])
                    trigger             = mission.add_trigger()
                    trigger.isActive    = True
                    trigger.triggerType = tokens[1]

                    cur = self.get_indent_level(mission.missionLines[i])
                    nxt = self.get_indent_level((mission.missionLines[i + 1]))
                    while True:
                        if nxt <= cur:
                            break
                        i, line = lines.__next__()
                        line = line.rstrip()
                        tokens = self.tokenize(line)

                        # dialog
                        if "dialog" in tokens[0]:
                            logging.debug("\t\t\tFound Dialog: %s" % tokens[1])
                            trigger.dialog = tokens[1]
                        elif "outfit" in tokens[0]:
                            logging.debug("\t\t\tFound Outfit: %s" % tokens)
                            self.store_component_data(trigger.outfit, tokens[1:])
                        elif "require" in tokens[0]:
                            logging.debug("\t\t\tFound Require: %s" % tokens)
                            self.store_component_data(trigger.require, tokens[1:])
                        elif "payment" in tokens[0]:
                            logging.debug("\t\t\tFound Outfit: %s" % tokens)
                            trigger.isPayment = True
                            self.store_component_data(trigger.payment, tokens[1:])
                        elif "event" in tokens[0]:
                            logging.debug("\t\t\tFound Event: %s" % tokens)
                            self.store_component_data(trigger.event, tokens[1:])
                        elif "fail" in tokens[0]:
                            logging.debug("\t\t\tFound Event: %s" % tokens[1])
                            trigger.isFail = True
                            trigger.fail   = tokens[1]
                        elif "log" in tokens[0] and len(tokens) == 2:
                            logging.debug("\t\t\tFound Log: %s" % tokens)
                            new_log            = trigger.add_log()
                            new_log.isActive   = True
                            new_log.formatType = "<message>"
                            new_log.log[0]     = tokens[1]
                        elif "log" in tokens[0]:
                            logging.debug("\t\t\tFound Log: %s" % tokens)
                            new_log            = trigger.add_log()
                            new_log.isActive   = True
                            new_log.formatType = "<type> <name> <message>"
                            self.store_component_data(new_log.log, tokens[1:])
                        elif tokens[1] in ["=", "+=", "-="]:
                            logging.debug("\t\t\tFound TriggerCondition: %s" % tokens)
                            new_tc               = trigger.add_tc()
                            new_tc.isActive      = True
                            new_tc.conditionType = 0
                            self.store_component_data(new_tc.condition, tokens)
                        elif tokens[1] in ["++", "--"]:
                            logging.debug("\t\t\tFound TriggerCondition: %s" % tokens)
                            new_tc               = trigger.add_tc()
                            new_tc.isActive      = True
                            new_tc.conditionType = 1
                            self.store_component_data(new_tc.condition, tokens)
                        elif tokens[0] in ["set", "clear"]:
                            logging.debug("\t\t\tFound TriggerCondition: %s" % tokens)
                            new_tc               = trigger.add_tc()
                            new_tc.isActive      = True
                            new_tc.conditionType = 2
                            self.store_component_data(new_tc.condition, tokens)
                        else:
                            logging.debug("Trigger component no found: ", i, line)
                        #end if/elif/else

                        try:
                            nxt = self.get_indent_level(mission.missionLines[i + 1])
                        except IndexError:
                            break
                    #end while
                else:
                    logging.debug("ERROR: No tokens found on line %d: %s" % (i, line))
                #end if/else
                for trigger in mission.components.triggerList:
                    trigger.print_trigger()
            #end for
        #end for

        logging.debug("File parsing complete.")
    #end run

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
    #end tokenize

    @staticmethod
    def get_indent_level(line):
        """
        Counts the number of tabs at the beginning of the string

        :param line: The string to be checked
        """
        tab_count = len(line) - len(line.lstrip(' '))
        return tab_count
    #end get_indent_level

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
    #end store_component_data

#end class MissionFileParser
