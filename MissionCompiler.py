''' MissionCompiler.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

This pulls the data the user has entered and stores it in the corresponding Mission object.

'''
import shlex

class MissionCompiler(object):

    def __init__(self, esmb):
        self.esmb = esmb
        self.mission = esmb.activeMission.components
    #end init


    def run(self):
        print("Compiling mission...")

        '''
            Zero out all the data in the mission component, then store what data is selected
            based on the value of the corresponding entry state
        '''

        # mission display name
        self.mission.missionDisplayName = None
        if self.esmb.displayNameEntryState.get():
            print("\tFound display name: " + self.esmb.displayName.get())
            self.mission.missionDisplayName = self.esmb.displayName.get()
        #end if

        # description
        self.mission.description = None
        if self.esmb.descriptionEntryState.get():
            print("\tFound description: " + self.esmb.description.get())
            self.mission.description = self.esmb.description.get()
        #end if

        # isBlocked
        self.mission.blocked = None
        if self.esmb.isBlockedEntryState.get():
            print("\tFound block: " + self.esmb.isBlockedMessage.get())
            self.mission.blocked = self.esmb.isBlockedMessage.get()
        #end if

        # deadline
        self.mission.deadline.isDeadline = False
        self.mission.deadline.deadline   = [None, None]
        if self.esmb.deadlineEntryState.get():
            print("\tFound deadline")
            self.mission.deadline.isDeadline = True
            if self.esmb.deadlineOptionalsEntryState.get():
                print("\t\tFound deadline message: " + self.esmb.deadlineOptionals.get())
                line = self.esmb.deadlineOptionals.get()
                tokens = shlex.split(line)
                self.mission.deadline.deadline[0] = tokens[0]
                self.mission.deadline.deadline[1] = tokens[1]
            #end if
        #end if

        # cargo
        self.mission.cargo.isCargo        = False
        self.mission.cargo.cargoType      = [None, None, None, None]
        self.mission.cargo.cargoIllegal   = [None, None]
        self.mission.cargo.isCargoStealth = False
        if self.esmb.cargoEntryState.get():
            print("\tFound cargo: " + self.esmb.cargo.get())
            self.mission.cargo.isCargo = True
            line = self.esmb.cargo.get()
            tokens = shlex.split(line)
            self.mission.cargo.cargoType[0] = tokens[0]
            self.mission.cargo.cargoType[1] = tokens[1]
            if self.esmb.cargoOptionalsEntryState.get():
                print("\t\tFound cargo optional modifiers: " + self.esmb.cargoOptionals.get())
                line = self.esmb.cargoOptionals.get()
                tokens = shlex.split(line)
                i = 2
                for token in tokens:
                    self.mission.cargo.cargoType[i] = token
                    i += 1
                #end for
            #end if
            if self.esmb.cargoIllegalEntryState.get():
                print("\t\tFound cargo illegal modifier: %s" % self.esmb.cargoFine.get())
                self.mission.cargo.cargoIllegal[0] = self.esmb.cargoFine.get()
                if self.esmb.cargoFineMessageEntryState.get():
                    print("\t\tFounnd cargo illegal message: %s" % self.esmb.cargoFineMessage.get())
                    self.mission.cargo.cargoIllegal[1] = self.esmb.cargoFineMessage.get()
                #end if
            #end if
            if self.esmb.cargoStealthEntryState.get():
                print("\t\tFound cargo stealth modifier")
                self.mission.cargo.isCargoStealth = True
            #end if
        #end if

        # passengers
        self.mission.passengers.isPassengers = False
        self.mission.passengers.passengers   = [None, None, None]
        if self.esmb.passengersEntryState.get():
            print("\tFound passengers: %s" % self.esmb.passengers.get())
            self.mission.passengers.isPassengers  = True
            self.mission.passengers.passengers[0] = self.esmb.passengers.get()
            if self.esmb.passengersOptionalsEntryState.get():
                print("\t\tFound passengers optional data: %s" % self.esmb.passengersOptionals.get())
                line = self.esmb.passengersOptionals.get()
                tokens = shlex.split(line)
                i = 1
                for token in tokens:
                    self.mission.passengers.passengers[i] = token
                    i += 1
                #end for
            #end if
        #end if

        # isInvisible
        self.mission.isInvisible = False
        if self.esmb.isInvisibleEntryState.get():
            print("\tFound mission invisible modifier")
            self.mission.isInvisible = True
        #end if

        # priorityLevel
        self.mission.priorityLevel = None
        if self.esmb.priorityLevelEntryState.get():
            print("\tFound priority level: %s" % self.esmb.rbPriorityValue.get())
            self.mission.priorityLevel = self.esmb.rbPriorityValue.get()
        #end if

        # whereShown
        self.mission.whereShown = None
        if self.esmb.whereShownEntryState.get():
            print("\tFound where shown: %s" % self.esmb.rbWhereShownValue.get())
            self.mission.whereShown = self.esmb.rbWhereShownValue.get()
        # end if

        # repeat
        self.mission.isRepeat = False
        self.mission.repeat   = None
        if self.esmb.repeatEntryState.get():
            print("\tFound repeat")
            self.mission.isRepeat = True
            if self.esmb.repeatOptionalsEntryState.get():
                print("\t\tFound repeat optionals modifier: %s" % self.esmb.repeatOptionals.get())
                self.mission.repeat = self.esmb.repeatOptionals.get()
            #end if
        #end if

        # clearance
        #TODO: fully implement this when filters are implemented
        self.mission.clearance.isClearance = False
        self.mission.clearance.clearance   = None
        if self.esmb.clearanceEntryState.get():
            print("\tFound clearance: %s" % self.esmb.clearanceOptionals.get())
            self.mission.clearance.isClearance = True
            self.mission.clearance.clearance   = self.esmb.clearanceOptionals.get()
        #end if

        # isInfiltrating
        self.mission.isInfiltrating = False
        if self.esmb.isInfiltratingEntryState.get():
            print("\tFound infiltrating")
            self.mission.isInfiltrating = True
        #end if

        # waypoint
        self.mission.waypoint = None
        if self.esmb.waypointEntryState.get():
            print("\tFound waypoint: %s" % self.esmb.waypoint.get())
            self.mission.waypoint = self.esmb.waypoint.get()
        #end if

        # stopover
        #TODO: fully implement this when filters are implemented
        self.mission.stopover.isStopover = False
        self.mission.stopover.stopover   = None
        if self.esmb.stopoverEntryState.get():
            print("\tFound stopover: %s" % self.esmb.stopover.get())
            self.mission.stopover.isStopover = True
            self.mission.stopover.stopover   = self.esmb.stopover.get()
        #end if

        # source
        #TODO: fully implement this when filters are implemented
        self.mission.source.isSource = False
        self.mission.source.source   = None
        if self.esmb.sourceEntryState.get():
            print("\tFound source: %s" % self.esmb.source.get())
            self.mission.source.isSource = True
            self.mission.source.source   = self.esmb.source.get()
        #end if

        # destination
        # TODO: fully implement this when filters are implemented
        self.mission.destination.isDestination = False
        self.mission.destination.destination   = None
        if self.esmb.destinationEntryState.get():
            print("\tFound source: %s" % self.esmb.destination.get())
            self.mission.destination.isDestination = True
            self.mission.destination.destination   = self.esmb.destination.get()
        # end if

        print("Done.")
        # call the parser to save the new data
        self.esmb.activeMission.parseMission()
    #end run


#end class MissionCompiler