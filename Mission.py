#TODO: add a data structure to contain conversations

class Mission(object):

    def __init__(self, missionName, default=False):
        if default is False:
            self.missionLines = []              # List of the mission text
            self.convoList    = []              # List of lists containing one
                                            # conversation section per element
            self.missionName  = missionName

            # TODO: Build a parse Mission Script
            self.parseMission()
            print("Loading mission:", self.missionName)
        else:
            self.setDefaultValues(self, missionName)
    #end init


    def setDefaultValues(self, missionName):
        #TODO: Implement this

        #TODO: Fill this from default mission
        self.missionLines = []      # List of the mission text

        # TODO: Fill this from default mission
        self.convoList = []         # List of lists containing one
                                    # conversation section per element
        self.missionName = missionName
        print("Default mission loaded...")

    #end setDefaultValues

    def addLine(self, line):
        self.missionLines.append(line)
    #end addLine


    def printMission(self):
        print(self.missionLines)
    #end printMission

#end class Mission