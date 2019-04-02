#TODO: add a data structure to contain conversations

import MissionComponents

class Mission(object):

    def __init__(self, missionName, default=False):
        #TODO: set up MissionComponents at launch
        print("Loading mission:", missionName)
        self.declareKeywords()
        self.components = MissionComponents.MissionComponents()

        if default is False:
            self.missionName  = missionName
            self.missionLines = []              # List of the mission text
            self.convoList    = []              # List of lists containing one
                                                # conversation section per element
        else:
            self.setDefaultValues(missionName)
            #self.parseMission()

        # TODO: Build a parseMission thing
        self.parseMission()
    #end init


    def setDefaultValues(self, missionName):
        #print("Loading Mission:", missionName)
        #TODO: Implement this

        #TODO: Fill this from default mission
        self.missionLines = []      # List of the mission text

        # TODO: Fill this from default mission
        self.convoList = []         # List of lists containing one
                                    # conversation section per element
        self.missionName = missionName
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
        print("Parsing mission...", end="\t\t")

        print("Done.")
    #end parseMission

#end class Mission