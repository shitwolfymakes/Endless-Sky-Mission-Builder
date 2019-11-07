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
import sys
import logging

from model import Mission
from src.gui.GUI import GUI
import src.utils as utils
import src.config as config
import src.singletons as singletons


class ESMB:
    """The application object"""
    def __init__(self):
        self.setup()
        self.gui = GUI()
    #end init


    def setup(self):
        self._logger_setup()
        logging.debug("Starting ESMB...")
        self._load_tooltips()
        self._setup_singletons()

        if "debug=True" in sys.argv:
            config.debugging = True
            config.mission_file_items.add_item(Mission("Debugging"))
            config.mission_file_items.items_list[0].type = "mission"
            config.active_item = config.mission_file_items.items_list[0]
        # end if
    #end setup


    @staticmethod
    def _logger_setup():
        # For some reason this for loop is required to get the outputting to a file working
        # See here: https://stackoverflow.com/a/49202811
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename='log.txt', filemode='w', level=logging.DEBUG)
    # end _logger_setup


    @staticmethod
    def _load_tooltips():
        config.tooltips_dict = utils.load_tooltips()
        logging.debug("\tTooltips loaded!")
    # end _load_tooltips


    @staticmethod
    def _setup_singletons():
        config.mission_file_items = singletons.MissionFileItems()
    #end _setup_singletons
#end class ESMB


def main():
    ESMB()
# end main


if __name__ == "__main__":
    main()
