""" TriggerParser.py
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


class TriggerParser(object):
    def __init__(self, mission):
        self.components = mission.components
        self.trigger = None
        self.lines = []
    #end init

    def run(self, trigger):
        logging.debug("\t\tParsing Trigger...")
        self.trigger = trigger

        # triggerType
        if self._has_trigger_type():
            logging.debug("\t\t\tParsing ...")

        # dialog
        if self._has_dialog():
            logging.debug("\t\t\tParsing ...")

        # TODO: HANDLE CONVERSATIONS HERE

        # outfit
        if self._has_outfit():
            logging.debug("\t\t\tParsing ...")

        # request
        if self._has_request():
            logging.debug("\t\t\tParsing ...")

        # payment
        if self._has_payment():
            logging.debug("\t\t\tParsing ...")

        # Conditions
        if self._has_conditions():
            logging.debug("\t\t\tParsing ...")

        # event
        if self._has_event():
            logging.debug("\t\t\tParsing ...")

        # fail
        if self._has_fail():
            logging.debug("\t\t\tParsing ...")

        # Logs
        if self._has_logs():
            logging.debug("\t\t\tParsing ...")

    #end run

    def _add_line(self, line):
        self.lines.append(line + "\n")
    # end add_line
#end class TriggerParser
