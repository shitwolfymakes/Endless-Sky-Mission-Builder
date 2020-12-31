""" Trigger.py
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

from model.components.TriggerCondition import TriggerCondition
from model.components.Log import Log

class Trigger:
    #TODO: Implement this - ~80% Complete
    # - still needs on enter [<system>]

    #TODO: Update to log conversations
    """
        Triggers:

        on (offer | complete | accept | decline | defer | fail | visit | stopover | enter [<system>])
            dialog <text>
            <text>...
            conversation <name>
            conversation
                ...
            outfit <outfit> [<count#>]
            require <outfit>
            payment [<base> [<multiplier>]]
            <condition> (= | += | -=) <value#>
            <condition> (++ | --)
            (set | clear) <condition>
            event <name> [<delay#> [<max#>]]
            fail [<name>]
    """

    def __init__(self):
        logging.debug("\t\tComponent %s initializing..." % self.__class__)

        self.is_active    = False
        self.trigger_type = None
        self.dialog       = None
        self.outfit       = [None, None]
        self.require      = [None, None]
        self.is_payment   = False
        self.payment      = [None, None]
        self.event        = [None, None, None]
        self.is_fail      = False
        self.fail         = None
        self.logs         = []
        self.conditions   = []
        self.convo_list   = []
    #end init


    def clear_trigger(self):
        """Zeroes out the data in the Trigger"""
        self.trigger_type = None
        self.dialog       = None
        self.outfit       = [None, None]
        self.require      = [None, None]
        self.is_payment   = False
        self.payment      = [None, None]
        self.event        = [None, None, None]
        self.is_fail      = False
        self.fail         = None
    #end clear_trigger


    def print_trigger(self):
        """Print the data all pretty-like"""
        logging.debug("\tTrigger Data")
        logging.debug("\t\tis_active: %s" % self.is_active)
        logging.debug("\t\tOn: %s" % self.trigger_type)
        logging.debug("\t\tDialog: %s" % self.dialog)
        logging.debug("\t\tOutfit: %s" % self.outfit)
        logging.debug("\t\tRequire: %s" % self.require)
        logging.debug("\t\tis_payment: %s" % self.is_payment)
        logging.debug("\t\tPayment: %s" % self.payment)
        logging.debug("\t\tEvent: %s" % self.event)
        logging.debug("\t\tis_fail: %s" % self.is_fail)
        logging.debug("\t\tFail: %s" % self.fail)
        logging.debug("\t\tLogs:")
        for log in self.logs:
            log.print_log()
        logging.debug("\t\tConditions:")
        for cond in self.conditions:
            cond.print_condition()
    #end print_trigger


    def add_log(self):
        """Add a log to this Trigger object"""
        new_log = Log()
        self.logs.append(new_log)
        logging.debug("\t\tLog %s added to %s" % (str(new_log), str(self)))
        return new_log
    #end add_log


    def remove_log(self, log):
        """Remove a log from this Trigger object"""
        logging.debug("\tRemoving %s from %s..." % (str(log), str(self)))
        self.logs.remove(log)
    #end remove_log


    def add_tc(self):
        """Add a TriggerCondition object to this Trigger object"""
        new_cond = TriggerCondition()
        self.conditions.append(new_cond)
        logging.debug("\t\tTriggerCondition %s added to %s" % (str(new_cond), str(self)))
        return new_cond
    #end add_log


    def remove_tc(self, condition):
        """Remove a TriggerCondition object to this Trigger object"""
        logging.debug("\tRemoving %s from %s..." % (condition, str(self)))
        self.conditions.remove(condition)
    #end remove_log


    def add_convo(self, convo):
        self.convo_list.append(convo)
        logging.debug("\t\tConversation %s added to %s" % (convo.name, str(self)))
    #end add_convo
#end class Trigger
