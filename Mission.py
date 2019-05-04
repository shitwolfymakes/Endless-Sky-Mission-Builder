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

        self.parseMission()
    #end init


    def setDefaultValues(self, missionName):
        #TODO: Implement this
        self.missionName = missionName
        self.addLine("mission \"%s\"\n" % missionName)
        self.addLine("\t-THIS IS A NEWLY CREATED DEFAULT MISSION\n")
        self.addLine("\t-REMOVE THIS AFTER PARSER IS DONE\n")
    #end setDefaultValues


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
        if self.components.isDeadline:
            line = "\tdeadline"
            if self.components.deadline[0] is not None:
                line = line + " " + self.components.deadline[0]
                if self.components.deadline[1] is not None:
                    line = line + " " + self.components.deadline[1]
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



















        print("Done.")
    #end parseMission

#end class Mission