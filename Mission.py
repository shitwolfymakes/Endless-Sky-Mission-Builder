""" Mission.py
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

import MissionComponents


class Mission(object):
    """The Mission class is the data structure that stores the data for an Endless Sky mission."""

    def __init__(self, mission_name, default=False):
        logging.debug("Building mission:", mission_name)

        self.components   = MissionComponents.MissionComponents()
        self.missionLines = []  # List of the mission text
        self.convoList    = []  # List of lists containing one conversation section per element

        if default is False:
            self.missionName  = mission_name
        else:
            self._set_default_values(mission_name)
        #end if/else

    #end init


    def _set_default_values(self, mission_name):
        """
        Set data to default values. This method should only run when ESMB is run with the debugging flag

        :param mission_name: The name of the mission
        """
        self.missionName = mission_name
        self.add_line("mission \"%s\"\n" % mission_name)
    #end _set_default_values


    def add_line(self, line):
        """
        Helper method for appending text to missionLines

        :param line: the string to be appended
        """
        self.missionLines.append(line + "\n")
    #end add_line


    def print_mission_to_console(self):
        """Helper method to print out the formatted text of the mission. e.g.: what it will look like when saved"""
        logging.debug(self.missionLines)
    #end printMission


    def print_mission_lines_to_text(self):
        """Concatenate all the missionLines together. Used to make a block of text to display in the missionFrame."""
        # Note to self: this is the most efficient and pythonic way to concat all these strings together
        mission_text = "".join(self.missionLines)
        return mission_text
    #end print_mission_lines_to_text


    def parse_mission(self):
        """This method parses the mission data(stored in components), formats it, and stores it in missionLines"""
        logging.debug("Parsing mission...", end="\t\t\t")
        self.missionLines = []          # empty the default values
        self.add_line("mission \"%s\"" % self.missionName)

        # mission display name
        if self.components.missionDisplayName is not None:
            self.add_line("\tname `%s`" % self.components.missionDisplayName)

        # description
        if self.components.description is not None:
            self.add_line("\tdescription `%s`" % self.components.description)

        # isBlocked
        if self.components.blocked is not None:
            self.add_line("\tblocked \"%s\"" % self.components.blocked)

        # deadline
        if self.components.deadline.isDeadline:
            line = "\tdeadline"
            if self.components.deadline.deadline[0] is not None:
                line = line + " " + self.components.deadline.deadline[0]
                if self.components.deadline.deadline[1] is not None:
                    line = line + " " + self.components.deadline.deadline[1]
                #end if
            #end if
            self.add_line(line)
        #end if

        # cargo
        if self.components.cargo.isCargo:
            line = "\tcargo"
            if self.components.cargo.cargo[0] is "random":
                line = line + " random"
            else:
                line = line + " \"%s\"" % self.components.cargo.cargo[0]
            #end if/else
            for part in self.components.cargo.cargo[1:]:
                if part is not None:
                    line = line + " " + part
                else:
                    break
                #end if/else
            #end for
            self.add_line(line)
        #end if

        # passengers
        if self.components.passengers.isPassengers:
            line = "\tpassengers %s" % self.components.passengers.passengers[0]
            for part in self.components.passengers.passengers[1:]:
                if part is not None:
                    line = line + " " + part
                else:
                    break
                #end if/else
            #end for
            self.add_line(line)
        #end if

        # illegal
        if self.components.illegal.isIllegal:
            line = "\tillegal %s" % self.components.illegal.illegal[0]
            if self.components.illegal.illegal[1] is not None:
                line = line + " `" + self.components.illegal.illegal[1] + "`"
            # end if
            self.add_line(line)
        #end if

        # stealth
        if self.components.isStealth:
            self.add_line("\tstealth")

        # isInvisible
        if self.components.isInvisible:
            self.add_line("\tinvisible")

        # priorityLevel
        if self.components.priorityLevel is not None:
            self.add_line("\t%s" % self.components.priorityLevel)

        # whereShown
        if self.components.whereShown is not None:
            self.add_line("\t%s" % self.components.whereShown)

        # repeat
        if self.components.isRepeat:
            line = "\trepeat"
            if self.components.repeat is not None:
                line = line + " " + self.components.repeat
            #end if
            self.add_line(line)
        #end if

        # clearance
        #TODO: fully implement this when filters are implemented
        if self.components.clearance.isClearance:
            self.add_line("\tclearance `%s`" % self.components.clearance.clearance)

        # isInfiltrating
        if self.components.isInfiltrating:
            self.add_line("\tinfiltrating")

        # waypoint
        if self.components.waypoint is not None:
            self.add_line("\twaypoint \"%s\"" % self.components.waypoint)

        # stopover
        #TODO: fully implement this when filters are implemented
        if self.components.stopover.isStopover:
            self.add_line("\tstopover \"%s\"" % self.components.stopover.stopover)

        # source
        #TODO: fully implement this when filters are implemented
        if self.components.source.isSource:
            self.add_line("\tsource \"%s\"" % self.components.source.source)

        # destination
        #TODO: fully implement this when filters are implemented
        if self.components.destination.isDestination:
            self.add_line("\tdestination \"%s\"" % self.components.destination.destination)

        # Trigger(s)
        for trigger in self.components.triggerList:
            if trigger.isActive:

                # triggerType
                if trigger.triggerType is not None:
                    self.add_line("\ton %s" % trigger.triggerType)

                # dialog
                if trigger.dialog is not None:
                    self.add_line("\t\tdialog `%s`" % trigger.dialog)

                # TODO: HANDLE CONVERSATIONS HERE

                # outfit
                if trigger.outfit[0] is not None:
                    line = "\t\toutfit "
                    line += self.add_quotes(trigger.outfit[0])
                    for data in trigger.outfit[1:]:
                        if data is None:
                            break
                        line = line + " " + data
                    #end for
                    self.add_line(line)
                #end if

                # request
                if trigger.require[0] is not None:
                    line = "\t\trequire "
                    line += self.add_quotes(trigger.require[0])
                    for data in trigger.require[1:]:
                        if data is None:
                            break
                        line = line + " " + data
                    # end for
                    self.add_line(line)
                # end if

                # payment
                if trigger.isPayment:
                    line = "\t\tpayment"
                    for data in trigger.payment:
                        if data is None:
                            break
                        line = line + " " + data
                    # end for
                    self.add_line(line)
                # end if

                # Conditions
                for condition in trigger.conditions:
                    if condition.isActive:
                        if condition.conditionType == 0:
                            self.add_line("\t\t\"%s\" %s %s" % (condition.condition[0], condition.condition[1], condition.condition[2]))
                        elif condition.conditionType == 1:
                            self.add_line("\t\t\"%s\" %s" % (condition.condition[0], condition.condition[1]))
                        elif condition.conditionType == 2:
                            self.add_line("\t\t%s \"%s\"" % (condition.condition[0], condition.condition[1]))
                        else:
                            logging.debug("Data corrupted!")
                        # end if/else
                    # end if
                # end for

                # event
                if trigger.event[0] is not None:
                    line = "\t\tevent "
                    line += self.add_quotes(trigger.event[0])
                    for data in trigger.event[1:]:
                        if data is None:
                            break
                        line = line + " " + data
                    # end for
                    self.add_line(line)
                # end if

                # fail
                if trigger.isFail:
                    line = "\t\tfail "
                    if trigger.fail is not None:
                        line += self.add_quotes(trigger.fail)
                    # end if
                    self.add_line(line)
                #end if

                # Logs
                for log in trigger.logs:
                    if log.isActive:
                        line = "\t\tlog"
                        if log.formatType == "<message>":
                            self.add_line("%s `%s`" % (line, log.log[0]))
                            continue
                        #end if
                        self.add_line("%s \"%s\" \"%s\" `%s`" % (line, log.log[0], log.log[1], log.log[2]))
                    #end if
                #end for

            #end if
        #end for

        logging.debug("Done.")
    #end parse_mission


    def add_trigger(self):
        """Add a trigger object to this mission"""
        new_trigger = MissionComponents.Trigger()
        self.components.triggerList.append(new_trigger)
        return new_trigger
    #end add_trigger


    def remove_trigger(self, trigger):
        """Remove a trigger object from this mission"""
        #print(trigger)
        self.components.triggerList.remove(trigger)
    #end remove_trigger


    @staticmethod
    def add_quotes(line):
        """
        Helper method to add quotes to a string

        :param line: The string to modify
        """
        if " " in line:
            line = "\"%s\"" % line
        return line
    #end add_quotes

#end class Mission
