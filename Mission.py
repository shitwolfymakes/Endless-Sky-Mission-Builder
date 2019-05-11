''' Mission.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.


'''

import MissionComponents

class Mission(object):

    def __init__(self, missionName, default=False):
        print("Building mission:", missionName)

        self.components   = MissionComponents.MissionComponents()
        self.missionLines = []  # List of the mission text
        self.convoList    = []  # List of lists containing one
                                # conversation section per element

        if default is False:
            self.missionName  = missionName
        else:
            self.setDefaultValues(missionName)
        #end if/else

    #end init


    def setDefaultValues(self, missionName):
        #TODO: Implement this
        self.missionName = missionName
        self.addLine("mission \"%s\"\n" % missionName)


    def addLine(self, line):
        self.missionLines.append(line + "\n")
    #end addLine


    def printMissionToConsole(self):
        print(self.missionLines)
    #end printMission


    def printMissionLinesToText(self):
        missionText = ""
        for line in self.missionLines:
            missionText+=str(line)
        return missionText
    #end printMissionLinesToText


    def parseMission(self):
        #TODO: IMPLEMENT THIS
        print("Parsing mission...", end="\t\t\t")
        self.missionLines = []          # empty the default values
        self.addLine("mission \"%s\"" % self.missionName)

        # mission display name
        if self.components.missionDisplayName is not None:
            self.addLine("\tname \"%s\"" % self.components.missionDisplayName)

        # description
        if self.components.description is not None:
            self.addLine("\tdescription \"%s\"" % self.components.description)

        # isBlocked
        if self.components.blocked is not None:
            self.addLine("\tblocked \"%s\"" % self.components.blocked)

        # deadline
        if self.components.deadline.isDeadline:
            line = "\tdeadline"
            if self.components.deadline.deadline[0] is not None:
                line = line + " " + self.components.deadline.deadline[0]
                if self.components.deadline.deadline[1] is not None:
                    line = line + " " + self.components.deadline.deadline[1]
                #end if
            #end if
            self.addLine(line)
        #end if

        # cargo
        if self.components.cargo.isCargo:
            line = "\tcargo"
            if self.components.cargo.cargoType[0] is "random":
                line = line + " random"
            else:
                line = line + " \"%s\"" % self.components.cargo.cargoType[0]
            #end if/else
            for part in self.components.cargo.cargoType[1:]:
                if part is not None:
                    line = line + " " + part
                else:
                    break
                #end if/else
            #end for
            self.addLine(line)
            if self.components.cargo.cargoIllegal[0] is not None:
                line = "\t\tillegal %s" % self.components.cargo.cargoIllegal[0]
                if self.components.cargo.cargoIllegal[1] is not None:
                    line = line + " " + self.components.cargo.cargoIllegal[1]
                #end if
                self.addLine(line)
            #end if
            if self.components.cargo.isCargoStealth:
                self.addLine("\t\tstealth")
        #end if

        # passengers
        if self.components.passengers.isPassengers:
            line = "\tpassengers %s" % self.components.passengers.passengers[0]
            for part in self.components.passengers.passengers[1:]:
                if part is not None:
                    line = line + " " + part
                else:
                    break
                #end if/else
            #end for
            self.addLine(line)
        #end if

        # isInvisible
        if self.components.isInvisible:
            self.addLine("\tinvisible")
        #end if

        # priorityLevel
        if self.components.priorityLevel is not None:
            self.addLine("\t%s" % self.components.priorityLevel)

        # whereShown
        if self.components.whereShown is not None:
            self.addLine("\t%s" % self.components.whereShown)

        # repeat
        if self.components.isRepeat:
            line = "\trepeat"
            if self.components.repeat is not None:
                line = line + " " + self.components.repeat
            #end if
            self.addLine(line)
        #end if

        # clearance
        #TODO: fully implement this when filters are implemented
        if self.components.clearance.isClearance:
            self.addLine("\tclearance `%s`" % self.components.clearance.clearance)

        # isInfiltrating
        if self.components.isInfiltrating:
            self.addLine("\tinfiltrating")

        # waypoint
        if self.components.waypoint is not None:
            self.addLine("\twaypoint \"%s\"" % self.components.waypoint)

        # stopover
        #TODO: fully implement this when filters are implemented
        if self.components.stopover.isStopover:
            self.addLine("\tstopover \"%s\"" % self.components.stopover.stopover)

        # source
        #TODO: fully implement this when filters are implemented
        if self.components.source.isSource:
            self.addLine("\tsource \"%s\"" % self.components.source.source)

        # destination
        #TODO: fully implement this when filters are implemented
        if self.components.destination.isDestination:
            self.addLine("\tdestination \"%s\"" % self.components.destination.destination)

        print("Done.")
    #end parseMission

#end class Mission