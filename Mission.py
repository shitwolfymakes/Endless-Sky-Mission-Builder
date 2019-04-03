#TODO: add a data structure to contain conversations

import MissionComponents

class Mission(object):

    def __init__(self, missionName, default=False):
        #TODO: set up MissionComponents at launch
        print("Loading mission:", missionName)

        self.components   = MissionComponents.MissionComponents()
        self.missionLines = []  # List of the mission text
        self.convoList    = []  # List of lists containing one
                                # conversation section per element

        if default is False:
            self.missionName  = missionName
        else:
            self.setDefaultValues(missionName)
            #self.parseMission()

        # TODO: Build a parseMission thing
        self.parseMission()
    #end init


    def setDefaultValues(self, missionName):
        #TODO: Implement this
        self.missionName = missionName

        #TODO: Fill missionLines from default mission

        #TODO: Fill convoList from default mission
    #end setDefaultValues


    def addLine(self, line):
        #TODO: IMPLEMENT THIS
        self.missionLines.append(line)
    #end addLine


    def printMissionToConsole(self):
        #TODO: IMPLEMENT THIS
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
        print("Done.")
    #end parseMission

#end class Mission