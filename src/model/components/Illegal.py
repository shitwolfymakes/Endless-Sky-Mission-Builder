""" Illegal.py
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


class Illegal(object):
    """
        self.illegal = [None, None] # illegal <fine> [<message>]
    """

    def __init__(self):
        logging.debug("\t\tComponent %s initializing..." % self.__class__)

        self.isActive = False
        self.illegal = [None, None]
    #end init


    def set(self, component_data):
        self.isActive = True
        for i, data in enumerate(component_data):
            self.illegal[i] = data
    #end set


    def reset(self):
        self.isActive = False
        self.illegal = [None, None]
    #end reset


    def to_string(self):
        line = "\tillegal %s" % self.illegal[0]
        if self.illegal[1] is not None:
            line += " `%s`" % self.illegal[1]
        return line
    #end to_string
#end class Illegal
