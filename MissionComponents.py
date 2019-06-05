''' MissionComponents.py
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
'''

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
    '''
        deadline = deadline [<days> [<multiplier>]]
    '''

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t")

        self.isDeadline = False
        self.deadline   = [None, None]

        print("Done.")
    # end init

# end class Deadline

class Cargo(object):
    '''
    cargo  = [None, None, None, None}    # cargo (random | <name>) <number> [<number> [<probability>]]
    '''

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t\t\t")

        self.isCargo        = False
        self.cargoType      = [None, None, None, None]

        print("Done.")
    #end init

#end class Cargo


class Passengers(object):
    '''
        self.passengers = [None, None, None] # passengers <number> [<number> [<probability>]]
    '''

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t")

        self.isPassengers = False
        self.passengers   = [None, None, None]

        print("Done.")
    # end init

# end class Passengers


class Illegal(object):
    '''
        self.illegal = [None, None] # illegal <fine> [<message>]
    '''

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t")

        self.isIllegal = False
        self.illegal   = [None, None]

        print("Done.")
    # end init

#end class Illegal


class Clearance(object):
    '''
    self.clearance = [[None, None],                # clearance [<message>]
                      [None, None]]                # attributes ...        ### THIS MAY NEED WORK ###
    '''

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t\t\t")

        self.isClearance = False
        self.clearance   = None

        print("Done.")
    # end init

# end class Clearance


class Stopover(object):
    '''
    self.stopover = [[None, None],                # stopover [<planet>]
                     [None, None]]                # attributes ...        ### THIS MAY NEED WORK ###
    '''

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t\t")

        self.isStopover = False
        self.stopover   = None

        print("Done.")
    # end init

# end class Conversations


class Source(object):
    '''
        Usage:
        (source) <planet>       # specific planet
        or
        (source)                filter
            ...
    '''

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t\t")

        self.isSource = False
        self.source   = [None, None]

        print("Done.")
    # end init

# end class Source


class Destination(object):
    '''
        Usage:
        (destination) <planet>       # specific planet
        or
        (destination)                filter
            ...
    '''

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t")

        self.isDestination = False
        self.destination   = [None, None]

        print("Done.")
    # end init

# end class Destination


class Trigger(object):
    #TODO: Implement this - ~50% Complete
    '''
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
    '''

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t")

        self.triggerType = None
        self.dialog      = None
        self.outfit      = [None, None]
        self.require     = [None, None]
        self.isPayment   = False
        self.payment     = [None, None]
        self.event       = [None, None, None]
        self.isFail      = False
        self.fail        = None

        print("Done.")
    #end init


    def clearTrigger(self):
        self.triggerType = None
        self.dialog = None
        self.outfit = [None, None]
        self.require = [None, None]
        self.isPayment = False
        self.payment = [None, None]
        self.event = [None, None, None]
        self.isFail = False
        self.fail = None
    #end clearTrigger


    def printTrigger(self):
        print(self.triggerType)
        print(self.dialog)
        print(self.outfit)
        print(self.require)
        print(self.isPayment)
        print(self.payment)
        print(self.event)
        print(self.isFail)
        print(self.fail)
    #end printTrigger

#end class Trigger


class Conversations(object):
    #TODO: Implement this in full in a separate tool

    def __init__(self):
        print("\t\tcomponent %s initializing..." % self.__class__, end="\t\t")
        print("Done.")
    # end init

# end class Conversations