# -*- coding: utf-8 -*-
###############################################################################
# This file is part of Resistencia Cadiz 1812.                                #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU General Public License as published by        #
# the Free Software Foundation, either version 3 of the License, or           #
# any later version.                                                          #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#                                                                             #
# Copyright (C) 2010, Pablo Recio Quijano, <pablo.recioquijano@alum.uca.es>   #
###############################################################################

import os.path
import random

import gtk

from resistencia import configure, xdg, filenames
from resistencia.nls import gettext as _
from resistencia.tests import selection

from guadaboard import human_game_handler

class humanGameDialog:
    
    def __init__(self, parent):
        self.rules_computer = ''
        self.formation_computer = ''
        self.formation_player = ''

        builder = gtk.Builder()
        builder.add_from_file(xdg.get_data_path('glade/humanEsDialog.glade'))

        def_path = configure.load_configuration()['se_path']
        def_rules_path = def_path + '/rules'
        def_formations_path = def_path + '/formations'

        self.human_ia_dialog = builder.get_object('human_ia_dialog')
        self.human_ia_dialog.set_transient_for(parent)
        
        builder.get_object('file_chooser_es_ia').set_current_folder(def_rules_path)
        builder.get_object('file_chooser_team_ia').set_current_folder(def_formations_path)
        builder.get_object('file_chooser_team').set_current_folder(def_formations_path)

        self.file_chooser_es_ia = builder.get_object('file_chooser_es_ia')
        self.file_chooser_team_ia = builder.get_object('file_chooser_team_ia')
        
        self.error_es_ia = builder.get_object("error_no_es_ia")
        self.error_es_ia.connect('response', lambda d, r: d.hide())
        self.error_es_ia.set_transient_for(self.human_ia_dialog)
        
        self.error_team_ia = builder.get_object("error_no_team_ia")
        self.error_team_ia.connect('response', lambda d, r: d.hide())
        self.error_team_ia.set_transient_for(self.human_ia_dialog)
        
        self.error_team = builder.get_object("error_no_team")
        self.error_team.connect('response', lambda d, r: d.hide())
        self.error_team.set_transient_for(self.human_ia_dialog)
        
        self.dlg_bad_file = builder.get_object('dlg_bad_file')
        self.dlg_bad_file.connect('response', lambda d, r: d.hide())
        self.dlg_bad_file.set_transient_for(self.human_ia_dialog)
        
        self.num_turns = 120
        self.spin_turns = builder.get_object("spin_num_turns")
        self.spin_turns.set_range(50,300)
        self.spin_turns.set_increments(1,10)
        self.spin_turns.set_value(self.num_turns)
        #---------------
        self.dont_save_game = False
        self.human_team = 'A'
        self.random_computer = False
        
        builder.connect_signals(self)

    def on_file_chooser_team_file_set(self, widget, data=None):
        self.formation_player = widget.get_uri().replace('file://', '')

    def on_file_chooser_es_ia_file_set(self, widget, data=None):
        self.rules_computer = widget.get_uri().replace('file://', '')

    def on_file_chooser_team_ia_file_set(self, widget, data=None):
        self.formation_computer = widget.get_uri().replace('file://', '')

    def on_radio_a_team_toggled(self, widget, data=None):
        if widget.get_active():
            self.human_team = 'A'

    def on_radio_b_team_toggled(self, widget, data=None):
        if widget.get_active():
            self.human_team = 'B'

    def on_check_random_team_toggled(self, widget, data=None):
        self.random_computer = widget.get_active()

        if self.random_computer:
            self.file_chooser_es_ia.set_sensitive(False)
            self.file_chooser_team_ia.set_sensitive(False)
        else:
            self.file_chooser_es_ia.set_sensitive(True)
            self.file_chooser_team_ia.set_sensitive(True)

    def on_spin_num_turns_change_value(self, widget, data=None):
        self.num_turns = int(widget.get_value())

    def on_spin_num_turns_value_changed(self, widget, data=None):
        self.num_turns = int(widget.get_value())

    def on_check_dont_save_toggled(self, widget):
        self.dont_save_game = widget.get_active()

    def on_human_ia_dialog_close(self, widget, data=None):
        self.human_ia_dialog.hide()
        
    def on_btn_cancel_clicked(self, widget, data=None):
        self.human_ia_dialog.hide()

    def on_btn_apply_clicked(self, widget, data=None):
        correct = True
        if len(self.formation_player) == 0:
            self.error_team.run()
            correct = False
        if len(self.rules_computer) == 0 and not self.random_computer:
            self.error_es_ia.run()
            correct = False
        if len(self.formation_computer) == 0 and not self.random_computer:
            self.error_team_ia.run()
            correct = False

        if correct:
            computer_team = None
            if self.random_computer:
                teams = selection.get_installed_teams()
                computer_team = teams[random.randint(0, len(teams)-1)]
            else:
                computer_team = (self.rules_computer, self.formation_computer)

            self.human_ia_dialog.destroy()
            while gtk.events_pending():
                gtk.main_iteration(False)
            try:
                human_game_handler.init_human_game(self.formation_player,
                                                   computer_team, self.human_team,
                                                   self.num_turns, self.dont_save_game)
                
            except human_game_handler.FileError as e:
                self.dlg_bad_file.format_secondary_text(e.msg)
                self.dlg_bad_file.run()
                self.quick_game.show()
                                  
            
