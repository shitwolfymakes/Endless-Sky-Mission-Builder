''' ESMB.py
Created by wolfy

Endless Sky Mission Builder aims to streamline the mission creation process,
so anyone can jump in and start making missions.

Endless Sky is made by Michael Zahniser.

My Github: https://github.com/shitwolfymakes
Endless Sky Github: https://github.com/endless-sky/endless-sky
'''

from GUI import *

class ESMB(object):

    def __init__(self):
        debugMode = False
        if "debug=True" in sys.argv:
            debugMode = True
        else:
            logfile = "log.txt"
            sys.stdout = open(logfile, 'w')
        self.gui = GUI(debugMode)
    #end init

#end class ESMB


def main():
    app = ESMB()
# end main


if __name__ == "__main__":
    main()