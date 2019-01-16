''' ESMB.py
Created by wolfy

Endless Sky Mission Builder aims to streamline the mission creation process,
so anyone can jump in and start making missions.

Endless Sky is made by Michael Zahniser.

My Github: https://github.com/shitwolfymakes
'''

from GUI import *

class ESMB(object):

    def __init__(self):
        self.gui = GUI()
    #end init

    #TODO: Where the fuck should I put this??
    '''
    def populateDict(self, componentDict):
        #TODO: consult the rock-paper-scissors game to declare dictionary
        componentDict.update({"mission": 1})
        componentDict.update({"name": 2})
        componentDict.update({"description": 3})
        componentDict.update({"blocked": 4})
        componentDict.update({"mission": 1})
        componentDict.update({"mission": 1})
    #end populateDict
    '''

#end class ESMB


def main():
    app = ESMB()
# end main


if __name__ == "__main__":
    main()