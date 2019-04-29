''' GUI.py
Created by wolfy

This pulls the data the user has entered and stores it in the corresponding Mission object

'''

class MissionCompiler(object):

    def __init__(self, esmb):
        self.esmb = esmb
        self.mission = esmb.activeMission.components
    #end init


    def run(self):
        print("Compiling mission...")

        # step through each Checkbutton's corresponding EntryState
        #   if selected, saved the data it guards

        # mission display name
        if self.esmb.displayNameEntryState.get() is True:
            print("\tFound display name: " + self.esmb.displayName.get())
            self.mission.missionDisplayName = self.esmb.displayName.get()

        # description
        if self.esmb.descriptionEntryState.get() is True:
            print("\tFound description: " + self.esmb.description.get())
            self.mission.description = self.esmb.description.get()

        # isBlocked
        if self.esmb.isBlockedEntryState.get() is True:
            print("\tFound block: " + self.esmb.isBlockedMessage.get())
            self.mission.blocked = self.esmb.isBlockedMessage.get()

        # deadline
        if self.esmb.deadlineEntryState.get() is True:
            print("\tFound deadline")
            self.mission.isDeadline = True
            if self.esmb.deadlineOptionalsEntryState.get() is True:
                print("\t\tFound deadline message: " + self.esmb.deadlineOptionals.get())
                line = self.esmb.deadlineOptionals.get()
                line.split()
                self.mission.deadline[0] = line[0]
                self.mission.deadline[1] = line[1]
            #end if
        #end if





        self.esmb.activeMission.parseMission()
        print("Mission compiled!")
    #end run


#end class MissionCompiler