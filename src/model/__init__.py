"""
model
=====

Provides
    1. A way to store mission data
    2. Ways to read in and write out mission data to files
    2. Take what is entered into the gui and store it into the model
"""
#TODO: restructure this package to have a subpackage for mission, event, and phrase
from .FileItem import FileItem
from .Mission import Mission
from .MissionCompiler import MissionCompiler
from .MissionComponents import MissionComponents

import model.components
