""" AggregatedSimpleEditorFrame.py
# Copyright (c) 2020 by Andrew Sneed
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
import src.widgets as widgets


class AggregatedSimpleEditorFrame(widgets.AggregatorFrame):
    def __init__(self, parent, title):
        logging.debug("\t\tBuilding AggregatedSimpleEditorFrame")
        widgets.AggregatorFrame.__init__(self, parent, title)
    #end init

    def add_frame(self):
        sef = widgets.SimpleEditorFrame(self, "Ship", 2, 0)
        self.frame_list.append(sef)
    # end add_frame


    def configure_frame(self):
        pass
    #end configure_frame
#end AggregatedSimpleEditorFrame
