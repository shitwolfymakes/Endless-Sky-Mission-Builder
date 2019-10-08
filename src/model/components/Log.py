""" Log.py
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


class Log:
    """This object stores data for Endless Sky logs"""

    def __init__(self):
        logging.debug("\t\tComponent %s initializing..." % self.__class__)

        self.is_active = False
        self.format_type = None
        self.log = [None, None, None]
    # end init


    def set(self, format_type, component_data):
        self.is_active = True

        if format_type == 1:
            self.format_type = "<message>"
        elif format_type == 3:
            self.format_type = "<type> <name> <message>"

        for i, data in enumerate(component_data):
            self.log[i] = data
    #end set


    def clear_log(self):
        """Zeroes out the data in the Log"""
        self.log = [None, None, None]
    #end clear_log


    def print_log(self):
        """Print the data all pretty-like"""
        logging.debug("\t\tLog Data")
        logging.debug("\t\t\tis_active: %s" % self.is_active)
        logging.debug("\t\t\tformat_type: %s" % self.format_type)
        logging.debug("\t\t\tLog: %s" % self.log)
    #end print_log
# end class Log
