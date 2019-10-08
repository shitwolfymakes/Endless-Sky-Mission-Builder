""" MissionFileItemsy
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


class MissionFileItems:
    """THis class provides a singleton that stores a list of FileObjects"""
    class __MissionFileObjects:
        def __init__(self):
            logging.debug("\tInitializing MissionFileItems...")
            self.items_list = []
            self.item_names = []
        #end init


        def __str__(self):
            return repr(self) + str(self.items_list)
        #end str


        def add_item(self, obj):
            self.items_list.append(obj)
            self.update_names()
        #end add_item


        def update_names(self):
            self.item_names = []
            for item in self.items_list:
                self.item_names.append(item.name)
        #end update_names


        def remove_item(self, obj):
            self.items_list.remove(obj)
        #end remove_item


        def get_names(self):
            name_list = []
            for obj in self.items_list:
                name_list.append(obj.name)
            return name_list
        #end get_names


        def get_item(self, name):
            for obj in self.items_list:
                if obj.name == name:
                    return obj
            #end for
        #end get_item
    #end class __MissionFileObjects

    instance = None

    def __init__(self):
        if not MissionFileItems.instance:
            MissionFileItems.instance = MissionFileItems.__MissionFileObjects()
        else:
            pass
        #end if/else
    #end init


    def __getattr__(self, name):
        return getattr(self.instance, name)
    #end getattr
#end class MissionFileItems
