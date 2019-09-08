""" MissionCompiler.py
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


class MissionCompiler(object):
    """This class compiles the data the user has entered into the current Mission object"""

    def __init__(self, esmb):
        self.esmb = esmb
        self.mission = esmb.activeMission.components
    #end init


    def run(self):
        """
        Zero the Mission data, then store what data is selected based on the value of the corresponding entry state
        """
        logging.debug("Compiling mission...")

        # mission display name
        self.mission.missionDisplayName = None
        if self.esmb.displayNameComponent.listEntryStates[0].get():
            logging.debug("\tFound display name: %s" % self.esmb.displayNameComponent.listEntryData[0].get())
            self.mission.missionDisplayName = self.esmb.displayNameComponent.listEntryData[0].get()
        #end if

        # description
        self.mission.description = None
        if self.esmb.descriptionComponent.listEntryStates[0].get():
            logging.debug("\tFound description: %s" % self.esmb.descriptionComponent.listEntryData[0].get())
            self.mission.description = self.esmb.descriptionComponent.listEntryData[0].get()
        #end if

        # isBlocked
        self.mission.blocked = None
        if self.esmb.blockedComponent.listEntryStates[0].get():
            logging.debug("\tFound block: %s" % self.esmb.blockedComponent.listEntryData[0].get())
            self.mission.blocked = self.esmb.blockedComponent.listEntryData[0].get()
        #end if

        # deadline
        self.mission.deadline.isDeadline = False
        self.mission.deadline.deadline   = [None, None]
        if self.esmb.deadlineComponent.listEntryStates[0].get():
            logging.debug("\tFound deadline")
            self.mission.deadline.isDeadline = True
            if self.esmb.deadlineComponent.listEntryStates[1].get():
                logging.debug("\t\tFound deadline days:" % self.esmb.deadlineComponent.listEntryData[0].get())
                self.mission.deadline.deadline[0] = self.esmb.deadlineComponent.listEntryData[0].get()
                if self.esmb.deadlineComponent.listEntryStates[2].get():
                    logging.debug("\t\tFound deadline message: %s" % self.esmb.deadlineComponent.listEntryData[1].get())
                    self.mission.deadline.deadline[1] = self.esmb.deadlineComponent.listEntryData[1].get()
                #end if
            #end if
        #end if

        # cargo
        self.mission.cargo.isCargo = False
        self.mission.cargo.cargo   = [None, None, None, None]
        if self.esmb.cargoComponent.listEntryStates[0].get():
            logging.debug("\tFound cargo:")
            logging.debug("\t\t%s" % self.esmb.cargoComponent.listEntryData[0].get())
            logging.debug("\t\t%s" % self.esmb.cargoComponent.listEntryData[1].get())
            self.mission.cargo.isCargo = True
            self.mission.cargo.cargo[0] = self.esmb.cargoComponent.listEntryData[0].get()
            self.mission.cargo.cargo[1] = self.esmb.cargoComponent.listEntryData[1].get()
            if self.esmb.cargoComponent.listEntryStates[1].get():
                logging.debug("\t\tFound cargo optional modifiers:")
                logging.debug("\t\t\t%s" % self.esmb.cargoComponent.listEntryData[2].get())
                self.mission.cargo.cargo[2] = self.esmb.cargoComponent.listEntryData[2].get()
                if self.esmb.cargoComponent.listEntryStates[2].get():
                    logging.debug("\t\t\t%s" % self.esmb.cargoComponent.listEntryData[3].get())
                    self.mission.cargo.cargo[3] = self.esmb.cargoComponent.listEntryData[3].get()
                #end if
            #end if
        #end if

        # passengers
        self.mission.passengers.isPassengers = False
        self.mission.passengers.passengers   = [None, None, None]
        if self.esmb.passengersComponent.listEntryStates[0].get():
            logging.debug("\tFound passengers: %s" % self.esmb.passengersComponent.listEntryData[0].get())
            self.mission.passengers.isPassengers  = True
            self.mission.passengers.passengers[0] = self.esmb.passengersComponent.listEntryData[0].get()
            if self.esmb.passengersComponent.listEntryStates[1].get():
                logging.debug("\t\tFound passengers optional data:")
                logging.debug("\t\t\t%s" % self.esmb.passengersComponent.listEntryData[1].get())
                self.mission.passengers.passengers[1] = self.esmb.passengersComponent.listEntryData[1].get()
                if self.esmb.passengersComponent.listEntryStates[2].get():
                    logging.debug("\t\t\t%s" % self.esmb.passengersComponent.listEntryData[2].get())
                    self.mission.passengers.passengers[2] = self.esmb.passengersComponent.listEntryData[2].get()
                #end if
            #end if
        #end if

        # illegal
        self.mission.illegal.isIllegal = False
        self.mission.illegal.illegal   = [None, None]
        if self.esmb.illegalComponent.listEntryStates[0].get():
            logging.debug("\tFound illegal: %s" % self.esmb.illegalComponent.listEntryData[0].get())
            self.mission.illegal.isIllegal  = True
            self.mission.illegal.illegal[0] = self.esmb.illegalComponent.listEntryData[0].get()
            if self.esmb.illegalComponent.listEntryStates[1].get():
                logging.debug("\t\tFound illegal optional modifier: %s" % self.esmb.illegalComponent.listEntryData[1].get())
                self.mission.illegal.illegal[1] = self.esmb.illegalComponent.listEntryData[1].get()
            # end if
        # end if

        # stealth
        self.mission.isStealth = False
        if self.esmb.stealthComponent.listEntryStates[0].get():
            logging.debug("\tFound stealth modifier")
            self.mission.isStealth = True
        # end if

        # isInvisible
        self.mission.isInvisible = False
        if self.esmb.invisibleComponent.listEntryStates[0].get():
            logging.debug("\tFound mission invisible modifier")
            self.mission.isInvisible = True
        #end if

        # priorityLevel
        self.mission.priorityLevel = None
        if self.esmb.priorityLevelComponent.isActive.get():
            logging.debug("\tFound priority level: %s" % self.esmb.priorityLevelComponent.combo.get().lower())
            self.mission.priorityLevel = self.esmb.priorityLevelComponent.combo.get().lower()
        #end if

        # whereShown
        self.mission.whereShown = None
        if self.esmb.whereShownComponent.isActive.get():
            logging.debug("\tFound where shown: %s" % self.esmb.whereShownComponent.combo.get().lower())
            self.mission.whereShown = self.esmb.whereShownComponent.combo.get().lower()
        # end if

        # repeat
        self.mission.isRepeat = False
        self.mission.repeat   = None
        if self.esmb.repeatComponent.listEntryStates[0].get():
            logging.debug("\tFound repeat")
            self.mission.isRepeat = True
            if self.esmb.repeatComponent.listEntryStates[1].get():
                logging.debug("\t\tFound repeat optionals modifier: %s" % self.esmb.repeatComponent.listEntryData[0].get())
                self.mission.repeat = self.esmb.repeatComponent.listEntryData[0].get()
            #end if
        #end if

        # clearance
        #TODO: fully implement this when filters are implemented
        self.mission.clearance.isClearance = False
        self.mission.clearance.clearance   = None
        if self.esmb.clearanceComponent.listEntryStates[0].get():
            logging.debug("\tFound clearance: %s" % self.esmb.clearanceComponent.listEntryData[0].get())
            self.mission.clearance.isClearance = True
            self.mission.clearance.clearance   = self.esmb.clearanceComponent.listEntryData[0].get()
        #end if

        # infiltrating
        self.mission.isInfiltrating = False
        if self.esmb.infiltratingComponent.listEntryStates[0].get():
            logging.debug("\tFound infiltrating")
            self.mission.isInfiltrating = True
        #end if

        # waypoint
        self.mission.waypoint = None
        if self.esmb.waypointComponent.listEntryStates[0].get():
            logging.debug("\tFound waypoint: %s" % self.esmb.waypointComponent.listEntryData[0].get())
            self.mission.waypoint = self.esmb.waypointComponent.listEntryData[0].get()
        #end if

        # stopover
        #TODO: fully implement this when filters are implemented
        self.mission.stopover.isStopover = False
        self.mission.stopover.stopover   = None
        if self.esmb.stopoverComponent.listEntryStates[0].get():
            logging.debug("\tFound stopover: %s" % self.esmb.stopoverComponent.listEntryData[0].get())
            self.mission.stopover.isStopover = True
            self.mission.stopover.stopover   = self.esmb.stopoverComponent.listEntryData[0].get()
        #end if

        # source
        #TODO: fully implement this when filters are implemented
        self.mission.source.isSource = False
        self.mission.source.source   = None
        if self.esmb.sourceComponent.listEntryStates[0].get():
            logging.debug("\tFound source: %s" % self.esmb.sourceComponent.listEntryData[0].get())
            self.mission.source.isSource = True
            self.mission.source.source   = self.esmb.sourceComponent.listEntryData[0].get()
        #end if

        # destination
        # TODO: fully implement this when filters are implemented
        self.mission.destination.isDestination = False
        self.mission.destination.destination   = None
        if self.esmb.destinationComponent.listEntryStates[0].get():
            logging.debug("\tFound source: %s" % self.esmb.destinationComponent.listEntryData[0].get())
            self.mission.destination.isDestination = True
            self.mission.destination.destination   = self.esmb.destinationComponent.listEntryData[0].get()
        # end if

        # Trigger data is compiled when TriggerWindow is closed

        logging.debug("Done.")
        # call the parser to save the new data
        self.esmb.activeMission.parse_mission()
    #end run

#end class MissionCompiler
