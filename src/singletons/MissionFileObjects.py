""" MissionFileObjects.py
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


class MissionFileObjects:
    """THis class provides a singleton that stores a list of FileObjects"""
    class __MissionFileObjects:
        def __init__(self):
            logging.debug("\tInitializing MissionFileObjects...")
            self.objects_list = []
        #end init


        def __str__(self):
            return repr(self) + str(self.objects_list)
        #end str


        def add_object(self, obj):
            self.objects_list.append(obj)
        #end add_object


        def remove_object(self, obj):
            self.objects_list.remove(obj)
        #end remove_object
    #end class __MissionFileObjects

    instance = None

    def __init__(self):
        if not MissionFileObjects.instance:
            MissionFileObjects.instance = MissionFileObjects.__MissionFileObjects()
        else:
            pass
        #end if/else
    #end init


    def __getattr__(self, name):
        return getattr(self.instance, name)
    #end getattr
#end class MissionFileObjects
