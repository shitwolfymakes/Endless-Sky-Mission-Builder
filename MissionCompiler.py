''' GUI.py
Created by wolfy

This pulls the data the user has entered and stores it in the corresponding Mission object.

'''
import shlex

class MissionCompiler(object):

    def __init__(self, esmb):
        self.esmb = esmb
        self.mission = esmb.activeMission.components
    #end init


    def run(self):
        print("Compiling mission...")

        '''
            Zero out all the data in the mission component, then store what data is selected
            based on the value of the corresponding entry state
        '''

        # mission display name
        self.mission.missionDisplayName = None
        if self.esmb.displayNameEntryState.get():
            print("\tFound display name: " + self.esmb.displayName.get())
            self.mission.missionDisplayName = self.esmb.displayName.get()
        #end if

        # description
        self.mission.description = None
        if self.esmb.descriptionEntryState.get():
            print("\tFound description: " + self.esmb.description.get())
            self.mission.description = self.esmb.description.get()
        #end if

        # isBlocked
        self.mission.blocked = None
        if self.esmb.isBlockedEntryState.get():
            print("\tFound block: " + self.esmb.isBlockedMessage.get())
            self.mission.blocked = self.esmb.isBlockedMessage.get()
        #end if

        # deadline
        self.mission.deadline.isDeadline = False
        self.mission.deadline.deadline   = [None, None]
        if self.esmb.deadlineEntryState.get():
            print("\tFound deadline")
            if self.esmb.deadlineOptionalsEntryState.get():
                print("\t\tFound deadline message: " + self.esmb.deadlineOptionals.get())
                line = self.esmb.deadlineOptionals.get()
                tokens = shlex.split(line)
                self.mission.deadline[0] = tokens[0]
                self.mission.deadline[1] = tokens[1]
            #end if
        #end if

        # cargo
        self.mission.cargo.isCargo        = False
        self.mission.cargo.cargoType      = [None, None, None, None]
        self.mission.cargo.cargoIllegal   = [None, None]
        self.mission.cargo.isCargoStealth = False
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
                    i += 1
                #end for
            #end if
            if self.esmb.cargoIllegalEntryState.get():
                print("\t\tFound cargo illegal modifier: %s" % self.esmb.cargoFine.get())
                self.mission.cargo.cargoIllegal[0] = self.esmb.cargoFine.get()
                if self.esmb.cargoFineMessageEntryState.get():
                    print("\t\tFounnd cargo illegal message: %s" % self.esmb.cargoFineMessage.get())
                    self.mission.cargo.cargoIllegal[1] = self.esmb.cargoFineMessage.get()
                #end if
            #end if
            if self.esmb.cargoStealthEntryState.get():
                print("\t\tFound cargo stealth modifier")
                self.mission.cargo.isCargoStealth = True
            #end if
        #end if

        # passengers
        self.mission.passengers.isPassengers = False
        self.mission.passengers.passengers   = [None, None, None]
        if self.esmb.passengersEntryState.get():
            print("\tFound passengers: %s" % self.esmb.passengers.get())
            self.mission.passengers.isPassengers  = True
            self.mission.passengers.passengers[0] = self.esmb.passengers.get()
            if self.esmb.passengersOptionalsEntryState.get():
                print("\t\tFound passengers optional data: %s" % self.esmb.passengersOptionals.get())
                line = self.esmb.passengersOptionals.get()
                tokens = shlex.split(line)
                i = 1
                for token in tokens:
                    self.mission.passengers.passengers[i] = token
                    i += 1
                #end for
            #end if
        #end if











        # call the parser to save the new data
        self.esmb.activeMission.parseMission()
        print("Mission compiled!")
    #end run


#end class MissionCompiler