''' GUI.py
Created by wolfy

This pulls the data the user has entered and stores it in the corresponding Mission object

'''

class MissionCompiler(object):

    def __init__(self, esmb):
        self.esmb = esmb
    #end init


    def run(self):
        print("Compiling mission...")

        print("Mission compiled!")
    #end run


#end class MissionCompiler