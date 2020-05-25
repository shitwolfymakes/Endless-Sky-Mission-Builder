""" Phrase.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
"""
import logging

import src.model as model


class Phrase(model.FileItem):
    #TODO: implement this
    def __init__(self, name):
        logging.debug("Building phrase %s", name)

        super().__init__("phrase")
        self.name = name

        self.parse()
    #end init


    def parse(self):
        pass
    #end parse
#end class Event
