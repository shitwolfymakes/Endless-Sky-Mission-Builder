''' ESMB.py
Created by wolfy

Endless Sky Mission Builder aims to streamline the mission creation process,
so anyone can jump in and start making missions.

Endless Sky is made by Michael Zahniser.

My Github: https://github.com/shitwolfymakes
'''

#TODO: Build a Directed Acyclic Graph library to store the conversation data (Version 2)
from GUI import *

class ESMB(object):

    def __init__(self):
        self.gui = GUI()
    #end init

#end class ESMB


def main():
    app = ESMB()
# end main


if __name__ == "__main__":
    main()