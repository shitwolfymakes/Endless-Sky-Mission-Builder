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


class TriggerParser():
    def __init__(self, mission):
        self.components = mission.components
        self.trigger = None
        self.lines = []
    #end init

    def run(self, trigger):
        self.trigger = trigger
        self.lines = []

        # isActive
        if self.trigger.isActive:
            logging.debug("\t\t\tParsing Trigger...")
        else:
            return ""
        #end if/else

        # triggerType
        if self._has_trigger_type():
            self._parse_trigger_type()

        # dialog
        if self._has_dialog():
            self._parse_dialog()

        # TODO: HANDLE CONVERSATIONS HERE

        # outfit
        if self._has_outfit():
            self._parse_outfit()

        # require
        if self._has_require():
            self._parse_require()

        # payment
        if self._has_payment():
            self._parse_payment()

        # Conditions
        if self._has_conditions():
            self._parse_conditions()

        # event
        if self._has_event():
            self._parse_event()

        # fail
        if self._has_fail():
            self._parse_fail()

        # Logs
        if self._has_logs():
            self._parse_logs()

        return self.lines
    #end run


    def _add_line(self, line):
        self.lines.append(line + "\n")
    # end add_line


    @staticmethod
    def _add_quotes(line):
        if " " in line:
            # if there is a space anywhere in the data piece, Endless Sky requires it to be inside quotations
            line = "\"%s\"" % line
        return line
    # end add_quotes


    ### methods to check if components are active
    def _has_trigger_type(self):
        if self.trigger.triggerType is None:
            return False
        return True
    #end _has_trigger_type


    def _has_dialog(self):
        if self.trigger.dialog is None:
            return False
        return True
    #end _has_dialog


    def _has_outfit(self):
        if self.trigger.outfit[0] is None:
            return False
        return True
    #end _has_outfit


    def _has_require(self):
        if self.trigger.require[0] is None:
            return False
        return True
    #end _has_request


    def _has_payment(self):
        if self.trigger.isPayment is False:
            return False
        return True
    #end _has_payment


    def _has_conditions(self):
        if not self.trigger.conditions:
            return False
        return True
    #end _has_conditions


    def _has_event(self):
        if self.trigger.event[0] is None:
            return False
        return True
    #end _has_event


    def _has_fail(self):
        if self.trigger.isFail is False:
            return False
        return True
    #end _has_fail


    def _has_logs(self):
        if not self.trigger.logs:
            return False
        return True
    #end _has_logs


    ### methods to parse the data from each component in the model
    def _parse_trigger_type(self):
        logging.debug("\t\t\tParsing trigger type...")
        self._add_line("\ton %s" % self.trigger.triggerType)
    #end _parse_trigger_type


    def _parse_dialog(self):
        logging.debug("\t\t\tParsing dialog...")
        self._add_line("\t\tdialog `%s`" % self.trigger.dialog)
    #end _parse_dialog


    def _parse_outfit(self):
        logging.debug("\t\t\tParsing outfit...")
        line = "\t\toutfit "
        line += self._add_quotes(self.trigger.outfit[0])
        for data in self.trigger.outfit[1:]:
            if data is None:
                break
            line += " %s" % str(data)
        # end for
        self._add_line(line)
    #end _parse_outfit


    def _parse_require(self):
        logging.debug("\t\t\tParsing require...")
        line = "\t\trequire "
        line += self._add_quotes(self.trigger.require[0])
        for data in self.trigger.require[1:]:
            if data is None:
                break
            line += " %s" % str(data)
        # end for
        self._add_line(line)
    #end _parse_require


    def _parse_payment(self):
        logging.debug("\t\t\tParsing payment...")
        line = "\t\tpayment"
        for data in self.trigger.payment:
            if data is None:
                break
            line += " %s" % str(data)
        # end for
        self._add_line(line)
    #end _parse_payment


    def _parse_conditions(self):
        logging.debug("\t\t\tParsing conditions...")
        for condition in self.trigger.conditions:
            if condition.isActive:
                if condition.conditionType == 0:
                    self._add_line("\t\t\"%s\" %s %s" % (condition.condition[0],
                                                         condition.condition[1],
                                                         condition.condition[2]))
                elif condition.conditionType == 1:
                    self._add_line("\t\t\"%s\" %s" % (condition.condition[0],
                                                      condition.condition[1]))
                elif condition.conditionType == 2:
                    self._add_line("\t\t%s \"%s\"" % (condition.condition[0],
                                                      condition.condition[1]))
                else:
                    logging.error("Condition data corrupted!")
                # end if/else
            # end if
        # end for
    #end _parse_conditions


    def _parse_event(self):
        logging.debug("\t\t\tParsing event...")
        line = "\t\tevent "
        line += self._add_quotes(self.trigger.event[0])
        for data in self.trigger.event[1:]:
            if data is None:
                break
            line += " %s" % str(data)
        # end for
        self._add_line(line)
    #end _parse_event


    def _parse_fail(self):
        logging.debug("\t\t\tParsing fail...")
        line = "\t\tfail "
        if self.trigger.fail is not None:
            line += self._add_quotes(self.trigger.fail)
        # end if
        self._add_line(line)
    #end _parse_fail


    def _parse_logs(self):
        logging.debug("\t\t\tParsing logs...")
        for log in self.trigger.logs:
            if log.isActive:
                line = "\t\tlog"
                if log.formatType == "<message>":
                    self._add_line("%s `%s`" % (line, log.log[0]))
                    continue
                # end if
                self._add_line("%s \"%s\" \"%s\" `%s`" % (line, log.log[0], log.log[1], log.log[2]))
            # end if
        # end for
    #end _parse_logs
#end class TriggerParser
