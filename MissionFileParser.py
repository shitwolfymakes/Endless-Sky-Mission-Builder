''' MissionFileParser.py
Created by wolfy

This takes the data read in from a mission file and stores it in each mission object

'''

class MissionFileParser(object):
    def __init__(self, esmb):
        self.esmb = esmb
        self.missions = esmb.missionList
    #end init

    def run(self):
        print("\nParsing Mission file...")

        print("Done.")
    #end run
#end class MissionFileParser