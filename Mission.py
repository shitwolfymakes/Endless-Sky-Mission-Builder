#TODO: add a data structure to contain conversations

import MissionComponents

class Mission(object):

    def __init__(self, missionName, default=False):
        #TODO: set up MissionComponents at launch
        print("Loading mission:", missionName)
        self.declareKeywords()

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


    def printMission(self):
        #TODO: IMPLEMENT THIS
        print(self.missionLines)
    #end printMission


    def parseMission(self):
        #TODO: IMPLEMENT THIS
        print("Parsing mission...", end="\t\t")

        print("Done.")
    #end parseMission


    def declareKeywords(self):
        #TODO: Implement this

        #TODO: convert the multipart keywords to bespoke objects
        ### DECLARE MISSION KEYWORDS ###
        missionDisplayName  = None                          # mission <name>
        description         = None                          # description <text>
        blocked             = None                          # blocked <message>
        deadline            = [ None, None ]                # deadline [<days> [<multiplier>]]
        cargo               = [ [None, None, [None, None]], # cargo (random | <name>) <number> [<number> [<probability>]]
                                [None, None, None],         #     illegal <fine> [<message>]
                                None ]                      #     stealth
        passengers          = [ None, None, None ]          # passengers <number> [<number> [<probability>]]
        isInvisible         = False                         # invisible
        priorityMinor       = None                          # (priority | minor)
        whereShown          = None                          # (job | landing | assisting | boarding)
        repeat              = None                          # repeat [<number>]
        clearance           = [ [None, None],               # clearance [<message>]
                                [None, None] ]              # attributes ...        ### THIS MAY NEED WORK ###
        isInfiltrating      = False                         # infiltrating
        waypoint            = None                          # waypoint <system>
        stopover            = [ [None, None],               # stopover [<planet>]
                                [None, None] ]              # attributes ...        ### THIS MAY NEED WORK ###


    #end declareKeywords

#end class Mission