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

import src.model as model


class Mission(object):
    """The Mission class is the data structure that stores the data for an Endless Sky mission."""

    def __init__(self, mission_name, default=False):
        #TODO: remove default case after new paser is complete
        logging.debug("Building mission: %s" % mission_name)

        self.components = model.MissionComponents()
        self.missionLines = []  # List of the mission text
        self.convoList = []  # List of lists containing one conversation section per element

        if default is False:
            self.missionName  = mission_name
        else:
            self.missionName = mission_name
            self.add_line("mission \"%s\"\n" % mission_name)
        #end if/else
    #end init


    def add_line(self, line):
        """
        Helper method for appending text to missionLines

        :param line: the string to be appended
        """
        self.missionLines.append(line + "\n")
    #end add_line


    def print_mission_to_console(self):
        """Helper method to print out the formatted text of the mission. e.g.: what it will look like when saved"""
        print(self.missionLines)
    #end printMission


    def print_mission_lines_to_text(self):
        """Concatenate all the missionLines together. Used to make a block of text to display in the missionFrame."""
        # Note to self: this is the most efficient and pythonic way to concat all these strings together
        mission_text = "".join(self.missionLines)
        return mission_text
    #end print_mission_lines_to_text


    def parse_mission(self):
        parser = model.MissionParser(self)
        self.missionLines = parser.run()

    def add_trigger(self):
        """Add a trigger object to this mission"""
        new_trigger = model.components.Trigger()
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
            # if there is a space anywhere in the data piece, Endless Sky requires it to be inside quotations
            line = "\"%s\"" % line
        return line
    #end add_quotes
#end class Mission
