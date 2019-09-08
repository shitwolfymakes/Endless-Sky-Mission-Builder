""" ESMB.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.


Endless Sky Mission Builder aims to streamline the mission creation process,
so anyone can jump in and start making missions.

Endless Sky is made by Michael Zahniser.

My Github: https://github.com/shitwolfymakes
Endless Sky Github: https://github.com/endless-sky/endless-sky
"""
#TODO: Implement logging
import logging

from GUI import *

debugMode = False


class ESMB(object):
    """The application object"""

    def __init__(self):
        if "debug=True" in sys.argv:
            global debugMode
            debugMode= True
        else:
            logging.basicConfig(filename='log.txt', level=logging.DEBUG)
        self.gui = GUI(debugMode)
    #end init

#end class ESMB


def main():
    ESMB()
# end main


if __name__ == "__main__":
    main()
