''' GUI.py
Created by wolfy

This pulls the data the user has entered and stores it in the corresponding Mission object

'''
import shlex

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
        if self.esmb.displayNameEntryState.get():
            print("\tFound display name: " + self.esmb.displayName.get())
            self.mission.missionDisplayName = self.esmb.displayName.get()

        # description
        if self.esmb.descriptionEntryState.get():
            print("\tFound description: " + self.esmb.description.get())
            self.mission.description = self.esmb.description.get()

        # isBlocked
        if self.esmb.isBlockedEntryState.get():
            print("\tFound block: " + self.esmb.isBlockedMessage.get())
            self.mission.blocked = self.esmb.isBlockedMessage.get()

        # deadline
        if self.esmb.deadlineEntryState.get():
            print("\tFound deadline")
            self.mission.isDeadline = True
            if self.esmb.deadlineOptionalsEntryState.get():
                print("\t\tFound deadline message: " + self.esmb.deadlineOptionals.get())
                line = self.esmb.deadlineOptionals.get()
                tokens = shlex.split(line)
                self.mission.deadline[0] = tokens[0]
                self.mission.deadline[1] = tokens[1]
            #end if
        #end if

        # cargo
        if self.esmb.cargoEntryState.get():
            print("\tFound cargo: " + self.esmb.cargo.get())
            self.mission.cargo.isCargo = True
            line = self.esmb.cargo.get()
            tokens = shlex.split(line)
            self.mission.cargo.cargoType[0] = tokens[0]
            self.mission.cargo.cargoType[1] = tokens[1]
            if self.esmb.cargoOptionalsEntryState.get():
                print("\t\tFound cargo optional modifiers: " + self.esmb.cargoOptionals.get())
                line = self.esmb.cargoOptionals.get()
                tokens = shlex.split(line)
                i = 2
                for token in tokens:
                    self.mission.cargo.cargoType[i] = token
                    i+=1
            if self.esmb.cargoIllegalEntryState.get():
                print("\t\tFound cargo illegal modifiers: %s %s" % (self.esmb.cargoFineEntry.get(),
                                                                    self.esmb.cargoFineMessageEntry.get()))


        self.esmb.activeMission.parseMission()
        print("Mission compiled!")
    #end run


#end class MissionCompiler