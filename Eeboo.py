#Embedded file name: /Users/versonator/Jenkins/live/Binary/Core_Release_64_static/midi-remote-scripts/Launchpad/Launchpad.py
from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import *
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement

#SIDE_NOTES = (8, 24, 40, 56, 72, 88, 104, 120)
#DRUM_NOTES = (41, 42, 43, 44, 45, 46, 47, 57, 58, 59, 60, 61, 62, 63, 73, 74, 75, 76, 77, 78, 79, 89, 90, 91, 92, 93, 94, 95, 105, 106, 107)

class Eeboo(ControlSurface):
    """ Script for Eeeboo's Controller """

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        self.log_message("Hello world!")
        self.show_message("Hack enabled! Let's get groove!")
        self.log_message("ok!")


    def _on_selected_scene_changed(self):
        self.log_message("Selected scene changed!")
        self.show_message("Hack enabled! Let's get groove!")
        self.log_message(Live.Song.Song.View.highlighted_clip_slot.canonical_parent())