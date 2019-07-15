""" MissionComponents.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

This file contains the classes defining some components of a mission
"""


class MissionComponents(object):

    def __init__(self):
        print("\tMission components initializing...")

        self.missionDisplayName = None          # mission <name>
        self.description        = None          # description <text>
        self.blocked            = None          # blocked <message>
        self.deadline           = Deadline()
        self.cargo              = Cargo()
        self.passengers         = Passengers()
        self.illegal            = Illegal()
        self.isStealth          = False
        self.isInvisible        = False         # invisible
        self.priorityLevel      = None          # (priority | minor)
        self.whereShown         = None          # (job | landing | assisting | boarding)
        self.isRepeat           = False
        self.repeat             = None          # repeat [<number>]
        self.clearance          = Clearance()
        self.isInfiltrating     = False         # infiltrating
        self.waypoint           = None          # waypoint <system>
        self.stopover           = Stopover()
        self.source             = Source()
        self.destination        = Destination()
        self.triggerList        = []

        print("\tDone.")
    #end init

#end class MissionComponents


class Deadline(object):
    """
        deadline = deadline [<days> [<multiplier>]]
    """

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t")

        self.isDeadline = False
        self.deadline   = [None, None]

        print("Done.")
    # end init

# end class Deadline


class Cargo(object):
    """
    cargo  = [None, None, None, None}    # cargo (random | <name>) <number> [<number> [<probability>]]
    """

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t\t\t")

        self.isCargo = False
        self.cargo   = [None, None, None, None]

        print("Done.")
    #end init

#end class Cargo


class Passengers(object):
    """
        self.passengers = [None, None, None] # passengers <number> [<number> [<probability>]]
    """

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t")

        self.isPassengers = False
        self.passengers   = [None, None, None]

        print("Done.")
    # end init

# end class Passengers


class Illegal(object):
    """
        self.illegal = [None, None] # illegal <fine> [<message>]
    """

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t")

        self.isIllegal = False
        self.illegal   = [None, None]

        print("Done.")
    # end init

#end class Illegal


class Clearance(object):
    """
    self.clearance = [[None, None],                # clearance [<message>]
                      [None, None]]                # attributes ...        ### THIS MAY NEED WORK ###
    """

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t\t\t")

        self.isClearance = False
        self.clearance   = None

        print("Done.")
    # end init

# end class Clearance


class Stopover(object):
    """
    self.stopover = [[None, None],                # stopover [<planet>]
                     [None, None]]                # attributes ...        ### THIS MAY NEED WORK ###
    """

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t\t")

        self.isStopover = False
        self.stopover   = None

        print("Done.")
    # end init

# end class Conversations


class Source(object):
    """
        Usage:
        (source) <planet>       # specific planet
        or
        (source)                filter
            ...
    """

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t\t")

        self.isSource = False
        self.source   = [None, None]

        print("Done.")
    # end init

# end class Source


class Destination(object):
    """
        Usage:
        (destination) <planet>       # specific planet
        or
        (destination)                filter
            ...
    """

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t")

        self.isDestination = False
        self.destination   = [None, None]

        print("Done.")
    # end init

# end class Destination


class Trigger(object):
    #TODO: Implement this - ~50% Complete
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
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t")

        self.isActive    = False
        self.triggerType = None
        self.dialog      = None
        self.outfit      = [None, None]
        self.require     = [None, None]
        self.isPayment   = False
        self.payment     = [None, None]
        self.event       = [None, None, None]
        self.isFail      = False
        self.fail        = None
        self.logs        = []
        self.conditions  = []

        print("Done.")
    #end init


    def clear_trigger(self):
        self.triggerType = None
        self.dialog      = None
        self.outfit      = [None, None]
        self.require     = [None, None]
        self.isPayment   = False
        self.payment     = [None, None]
        self.event       = [None, None, None]
        self.isFail      = False
        self.fail        = None
    #end clear_trigger


    def print_trigger(self):
        print("\n\tTrigger Data")
        print("\t\tisActive:", self.isActive)
        print("\t\tOn:", self.triggerType)
        print("\t\tDialog:", self.dialog)
        print("\t\tOutfit:", self.outfit)
        print("\t\tRequire:", self.require)
        print("\t\tisPayment:", self.isPayment)
        print("\t\tPayment:", self.payment)
        print("\t\tEvent:", self.event)
        print("\t\tisFail:", self.isFail)
        print("\t\tFail:", self.fail)
        print("\t\tLogs:")
        for log in self.logs:
            log.print_log()
        print("\t\tConditions:")
        for cond in self.conditions:
            cond.print_condition()
        print()
    #end print_trigger


    def add_log(self):
        new_log = Log()
        self.logs.append(new_log)
        print("\t\tLog", new_log, "added to", self)
        return new_log
    #end add_log


    def remove_log(self, log):
        print("\t\tRemoving", log, "from", self, "...", end="\t\t")
        self.logs.remove(log)
        print("Done.")
    #end remove_log


    def add_tc(self):
        new_cond = TriggerCondition()
        self.conditions.append(new_cond)
        print("\t\tTriggerCondition", new_cond, "added to", self)
        return new_cond
    #end add_log


    def remove_tc(self, condition):
        print("\t\tRemoving", condition, "from", self, "...", end="\t\t")
        self.conditions.remove(condition)
        print("Done.")
    #end remove_log

#end class Trigger


class Log(object):

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t\t")

        self.isActive   = False
        self.formatType = None
        self.log        = [None, None, None]

        print("Done.")
    # end init


    def clear_log(self):
        self.log = [None, None, None]
    #end clear_log


    def print_log(self):
        print("\t\tLog Data")
        print("\t\t\tisActive:", self.isActive)
        print("\t\t\tformatType:", self.formatType)
        print("\t\t\tLog:", self.log)
    #end print_log

# end class Log


class TriggerCondition(object):

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t\t")

        self.isActive      = False
        self.conditionType = None
        self.condition     = [None, None, None]

        print("Done.")
    # end init


    def clear_condition(self):
        self.condition = [None, None, None]
    #end clearConditions


    def print_condition(self):
        print("\t\tCondition Data")
        print("\t\t\tisActive:", self.isActive)
        print("\t\t\tconditionType:", self.conditionType)
        print("\t\t\tCondition:", self.condition)
    #end printConditions

# end class TriggerConditions


class Conversations(object):
    #TODO: Implement this in full in a separate tool

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t\t")
        print("Done.")
    # end init

# end class Conversations
