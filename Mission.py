#TODO: add a data structure to contain conversations

class Mission(object):

    def __init__(self, missionName, default=False):
        if default is False:
            print("Loading mission:", missionName)
            self.missionLines = []              # List of the mission text
            self.convoList    = []              # List of lists containing one
                                                # conversation section per element
            self.missionName  = missionName

            # TODO: Build a parse Mission Script
            self.parseMission()
        else:
            self.setDefaultValues(self, missionName)
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
        self.missionLines.append(line)
    #end addLine


    def printMission(self):
        print(self.missionLines)
    #end printMission


    def parseMission(self):
        print("Parsing mission...", end="\t\t")

        print("Done.")
    #end parseMission

#end class Mission