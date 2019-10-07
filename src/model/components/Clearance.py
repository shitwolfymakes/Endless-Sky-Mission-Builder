""" Clearance.py
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


class Clearance:
    # TODO: fully implement this when filters are implemented
    """
    self.clearance = [[None, None],                # clearance [<message>]
                      [None, None]]                # attributes ...        ### THIS MAY NEED WORK ###
    """

    def __init__(self):
        logging.debug("\t\tComponent %s initializing..." % self.__class__)

        self.isActive = False
        self.clearance = None
    #end init


    def set(self, component_data):
        self.isActive = True
        self.clearance = component_data
    #end set


    def reset(self):
        self.isActive = False
        self.clearance = None
    #end reset


    def to_string(self):
        line = "\tclearance `%s`" % self.clearance
        return line
#end class Clearance
