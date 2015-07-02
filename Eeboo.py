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
    """ Script for Eeboo's Controller """

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        self._clip = None
        self.log_message(" ------ ")
        self.show_message("Hack enabled! Let's get groove!")
        self.song().view.add_detail_clip_listener(self._on_selected_clip)

    
    def _on_selected_clip(self):

        self.log_message(" _on_selected_clip ")

        # add_detail_clip_listener is triggered even slot is empty
        if self.song().view.detail_clip != None:

            # remove listener
            if self._clip != None:
                if self._clip.playing_status_has_listener(self._on_playing_status_changed):
                    self._clip.remove_playing_status_listener(self._on_playing_status_changed)
                if self._clip.playing_position_has_listener(self._on_playing_position_changed):
                    self._clip.remove_playing_position_listener(self._on_playing_position_changed)


            # new value
            self._clip = self.song().view.detail_clip

            # add listener
            if self._clip.is_midi_clip:
                self._clip.add_playing_status_listener(self._on_playing_status_changed)
                self._clip.add_playing_position_listener(self._on_playing_position_changed)


    def _on_playing_status_changed(self):
        self.log_message( " on_playing_status_changed: "  )
        if self._clip.is_playing:
            self.show_message("clip playing")

    def _on_playing_position_changed(self):
        self.log_message( " _on_playing_position_changed: "  )
        self.log_message( self._clip.playing_position )


    def _playing_clip_slot(self):
        track = self.song().view.selected_track
        try:
            playing_slot_index = track.playing_slot_index
            slot = track.clip_slots[playing_slot_index] if 0 <= playing_slot_index < len(track.clip_slots) else None
            return slot
        except RuntimeError:
            pass