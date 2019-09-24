""" Passengers.py
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


class Passengers(object):
    """
        self.passengers = [None, None, None] # passengers <number> [<number> [<probability>]]
    """

    def __init__(self):
        logging.debug("\t\tComponent %s initializing..." % self.__class__)

        self.isActive = False
        self.passengers = [None, None, None]
    #end init


    def set(self, component_data):
        self.isActive = True
        for i, data in enumerate(component_data):
            self.passengers[i] = data
    #end set


    def reset(self):
        self.isActive = False
        self.passengers = [None, None, None]
    #end reset


    def to_string(self):
        line = "\tpassengers %s" % self.passengers[0]
        for part in self.passengers[1:]:
            if part is not None:
                line += " %s" % str(part)
            else:
                break
            # end if/else
        # end for
        return line
    #end to_string
#end class Passengers
