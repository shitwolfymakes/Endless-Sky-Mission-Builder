"""
widgets
===========

Provides custom widgets to encapsulate complex, common parts of ESMB's gui

NOTE: the top level of this module should only contain classes that are use or inherited
by the classes in any submodules
"""
#TODO: Move the Trigger stuff to a submodule, like I have with NPC

from .AggregatorFrame import AggregatorFrame
from .AggregatedDialogFrame import AggregatedDialogFrame
from .AggregatedLogFrame import AggregatedLogFrame
from .AggregatedSimpleEditorFrame import AggregatedSimpleEditorFrame
from .AggregatedTriggerFrame import AggregatedTriggerFrame
from .AggregatedTriggerConditionFrame import AggregatedTriggerConditionFrame
from .ComboComponentFrame import ComboComponentFrame
from .ComponentMandOptFrame import ComponentMandOptFrame
from .DefaultTextEntry import DefaultTextEntry
from .DialogFrame import DialogFrame
from .SimpleEditorFrame import SimpleEditorFrame
from .LogFrame import LogFrame
from .LogWindow import LogWindow
from .MultiOptionFrame import MultiOptionFrame
from .NewMissionPopup import NewMissionPopup
from .ScrollingFrame import ScrollingFrame
from .Tooltip import Tooltip
from .TooltipLabel import TooltipLabel
from .TriggerConditionWindow import TriggerConditionWindow
from .TriggerConditionFrame import TriggerConditionFrame
from .TriggerFrame import TriggerFrame
from .TriggerWindow import TriggerWindow
from .TypeSelectorWindow import TypeSelectorWindow
