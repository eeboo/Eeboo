#Embedded file name: /Users/versonator/Jenkins/live/Binary/Core_Release_64_static/midi-remote-scripts/Launchpad/Launchpad.py
from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import *
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from eeboo_utils import make_button

#SIDE_NOTES = (8, 24, 40, 56, 72, 88, 104, 120)
#DRUM_NOTES = (41, 42, 43, 44, 45, 46, 47, 57, 58, 59, 60, 61, 62, 63, 73, 74, 75, 76, 77, 78, 79, 89, 90, 91, 92, 93, 94, 95, 105, 106, 107)

IS_MOMENTARY=True

class Eeboo(ControlSurface):
    """ Script for Eeboo's Controller """
    __module__=__name__                  #name of the class
    __doc__="Eeboo function"           #documentation 

    def __init__(self, c_instance):
        super(Eeboo, self).__init__(c_instance)
        with self.component_guard():               #don't know the us of this, but it is recquiered in live 9 scripts
            self.__c_instance = c_instance
            self.Pad1=ButtonElement(IS_MOMENTARY, MIDI_NOTE_TYPE, 0,60) # identifies P&d1 as a ButtonElement. IS_MOMENTARY is true if the button send a message on being released

            self.show_message("Hack enabled! Let's get groove!")

            ############ TODO => use it ######### 
            self._clip = None
            self._is_active = True
            self._playing_position_buttons = True
            self._is_following = True
        
            self._quantization = 0.25
        
            # Playhead current position
            self._row_index = None
            self._column_index = None

            # number of buttons per row
            self._width = 8

            # number of row of 8 buttons
            self.bank_display_capabilities = 2
            #####################################
        
            
            row_1 = [ make_button(1, 36 + idx) for idx in reversed(xrange(8)) ]
            row_2 = [ make_button(1, 45 + idx) for idx in reversed(xrange(8)) ]
            self._side_buttons = ButtonMatrixElement(name='Scene_Launch_Buttons', rows=[ row_1, row_2 ])
            self.show_message( "width: " +  str( self._side_buttons.width() ) )
            self.log_message( "width: " +  str( self._side_buttons.width() ) )

            button = ButtonElement(True, MIDI_CC_TYPE, 0, 36, name='button_name')

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
            self.show_message( "clip playing" )

    def _on_playing_position_changed(self):
        self.__on_playing_position_changed()

    def is_enabled(self):
    	return True



    def __on_playing_position_changed(self): #playing position changed listener
        if self.is_enabled() and self._is_active:
            self._sequencer_clip = self._clip
            if self._playing_position_buttons != None:
                if self._sequencer_clip != None:
                    """LiveAPI clip.playing_position: Constant access to the current playing position of the clip.
                    The returned value is the position in beats for midi and warped audio clips,
                    or in seconds for unwarped audio clips. Stopped clips will return 0."""
                    position = self._sequencer_clip.playing_position #position in beats (1/4 notes in 4/4 time)
                    
                    row = int(position / self._quantization / self._width) # 0.25 for 16th notes;  0.5 for 8th notes
                    #if self._is_following == True:
                        #if self._row_index != row:
                            #self._row_index = row
                            #self._update_bank_buttons()
                            #self._update_matrix()
                    
                    column = int(position / self._quantization) - (row * self._width) #stepped postion



                    """for index in range(self._width):
                        if index == grid_position and grid_position < self._width and self._bank_index == bank:
                            self._playing_position_buttons[index].turn_on()
                        else:
                            self._playing_position_buttons[index].turn_off()"""
                    self.log_message( 'column:' + str(column) )
                    self.log_message( 'row:' + str(row) )