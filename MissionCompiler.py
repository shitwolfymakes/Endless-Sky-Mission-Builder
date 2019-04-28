''' GUI.py
Created by wolfy

This pulls the data the user has entered and stores it in the corresponding Mission object

'''

class MissionCompiler(object):

    def __init__(self, esmb):
        self.esmb = esmb
        self.mission = esmb.activeMission
    #end init


    def run(self):
        print("Compiling mission...")

        # step through each Checkbutton's corresponding EntryState
        #   if selected, saved the data it guards
        if self.esmb.displayNameEntryState:
            print("Found display name: " + self.esmb.displayName.get())
            self.mission.components.missionDisplayName = self.esmb.displayName.get()




        self.mission.parseMission()
        print("Mission compiled!")
    #end run


#end class MissionCompiler