""" TriggerCondition.py
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


class TriggerCondition:
    """This object stores data for condition modifiers inside Endless Sky triggers"""

    def __init__(self):
        logging.debug("\t\tComponent %s initializing..." % self.__class__)

        self.is_active      = False
        self.condition_type = None
        self.condition      = [None, None, None]
    # end init


    def set(self, condition_type, component_data):
        self.is_active = True
        self.condition_type = condition_type
        for i, data in enumerate(component_data):
            self.condition[i] = data
    #end set


    def clear_condition(self):
        """Zeroes out the data in the TriggerCondition"""
        self.condition = [None, None, None]
    #end clearConditions


    def print_condition(self):
        """Print the data all pretty-like"""
        logging.debug("\t\tCondition Data")
        logging.debug("\t\t\tis_active: %s" % self.is_active)
        logging.debug("\t\t\tcondition_type: %s" % self.condition_type)
        logging.debug("\t\t\tCondition: %s" % self.condition)
    #end printCondition
# end class TriggerCondition
