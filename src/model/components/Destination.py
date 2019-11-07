""" Destination.py
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


class Destination:
    # TODO: fully implement this when filters are implemented
    """
        Usage:
        (destination) <planet>       # specific planet
        or
        (destination)                filter
            ...
    """

    def __init__(self):
        logging.debug("\t\tComponent %s initializing..." % self.__class__)

        self.is_active = False
        self.destination = None
    # end init


    def set(self, component_data):
        self.is_active = True
        self.destination = component_data
    #end set


    def reset(self):
        self.is_active = False
        self.destination = None
    #end reset


    def to_string(self):
        line = "\tdestination \"%s\"" % self.destination
        return line
    #end to_string
# end class Destination
