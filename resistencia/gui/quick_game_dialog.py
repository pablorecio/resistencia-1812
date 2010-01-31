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

import sys
import os.path

import gtk

from guadaboard import guada_board
from resistencia import configure, xdg, filenames

class quickGameDialog:    
    def __init__(self, parent):
        self.es_team_a = ''
        self.team_team_a = ''
        self.es_team_b = ''
        self.team_team_b = ''
        
        builder = gtk.Builder()
        builder.add_from_file(xdg.get_data_path('glade/quickGame.glade'))

        def_path = configure.load_configuration()['se_path']
        def_rules_path = def_path + '/rules'
        def_formations_path = def_path + '/formations'
        builder.get_object('file_chooser_es_a').set_current_folder(def_rules_path)
        builder.get_object('file_chooser_team_a').set_current_folder(def_formations_path)
        builder.get_object('file_chooser_es_b').set_current_folder(def_rules_path)
        builder.get_object('file_chooser_team_b').set_current_folder(def_formations_path)

        self.quick_game = builder.get_object("quickGameDialog")
        self.quick_game.set_transient_for(parent)
        #---- Initialation for the dialogs
        self.error_es_a = builder.get_object("error_no_es_a")
        self.error_es_a.connect('response', lambda d, r: d.hide())
        self.error_es_a.set_transient_for(self.quick_game)
        
        self.error_team_a = builder.get_object("error_no_team_a")
        self.error_team_a.connect('response', lambda d, r: d.hide())
        self.error_team_a.set_transient_for(self.quick_game)
        
        self.error_es_b = builder.get_object("error_no_es_b")
        self.error_es_b.connect('response', lambda d, r: d.hide())
        self.error_es_b.set_transient_for(self.quick_game)
        
        self.error_team_b = builder.get_object("error_no_team_b")
        self.error_team_b.connect('response', lambda d, r: d.hide())
        self.error_team_b.set_transient_for(self.quick_game)

        self.result_dialog = builder.get_object("dlg_result")
        self.result_dialog.connect('response', lambda d, r: d.hide())
        self.result_dialog.set_transient_for(self.quick_game)

        self.num_turns = 120
        self.spin_turns = builder.get_object("spin_num_turns")
        self.spin_turns.set_value(self.num_turns)
        self.spin_turns.set_range(50,300)
        self.spin_turns.set_increments(1,10)
        #---------------
        self.fast_game = False
        self.dont_save_game = False
        self.hidde_values = False
        
        builder.connect_signals(self)
        
    def on_quickGameDialog_close(self, widget, data=None):
        self.quick_game.hide()

    def on_file_chooser_es_a_file_set(self, widget, data=None):
        self.es_team_a = widget.get_uri()

    def on_file_chooser_team_a_file_set(self, widget, data=None):
        self.team_team_a = widget.get_uri()
        
    def on_file_chooser_es_b_file_set(self, widget, data=None):
        self.es_team_b = widget.get_uri()

    def on_file_chooser_team_b_file_set(self, widget, data=None):
        self.team_team_b = widget.get_uri()

    def on_check_fastgame_toggled(self, widget):
        self.fast_game = widget.get_active()

    def on_check_dont_save_toggled(self, widget):
        self.dont_save_game = widget.get_active()

    def on_check_hide_values_toggled(self, widget):
        self.hidde_values = widget.get_active()

    def on_spin_num_turns_change_value(self, widget, data=None):
        self.num_turns = widget.get_value()

    def on_spin_num_turns_value_changed(self, widget, data=None):
        self.num_turns = widget.get_value()
        
    def on_btn_cancel_clicked(self, widget, data=None):
        self.quick_game.hide()

    def on_btn_apply_clicked(self, widget, data=None):
        correct = True
        if len(self.es_team_a) == 0:
            self.error_es_a.show()
            correct = False
        else:
            self.es_team_a = self.es_team_a[7:]
            print self.es_team_a
            
        if len(self.es_team_b) == 0:
            self.error_es_b.show()
            correct = False
        else:
            self.es_team_b = self.es_team_b[7:]
            print self.es_team_b
            
        if len(self.team_team_a) == 0:
            self.error_team_a.show()
            correct = False
        else:
            self.team_team_a = self.team_team_a[7:]
            print self.team_team_a
            
        if len(self.team_team_b) == 0:
            self.error_team_b.show()
            correct = False
        else:
            self.team_team_b = self.team_team_b[7:]
            print self.team_team_b

        if correct == True:
            self.quick_game.hide()
            while gtk.events_pending():
                gtk.main_iteration(False)
            self.load_board()

    def load_board(self):
        winner = guada_board.run(((self.es_team_a,self.team_team_a),
                                  xdg.get_data_path('images/piece-orange.png')),
                                 ((self.es_team_b,self.team_team_b),
                                  xdg.get_data_path('images/piece-violete.png')),
                                 self.fast_game, self.dont_save_game,
                                 self.hidde_values, str(int(self.num_turns)))
        if self.fast_game:
            result = ''
            name_teamA = filenames.extract_name_expert_system((self.es_team_a,
                                                               self.team_team_a))
            name_teamB = filenames.extract_name_expert_system((self.es_team_b,
                                                               self.team_team_b))
            if winner == 0:
                result = 'Empate'
            elif winner == 1:
                result = 'Gana ' + name_teamA
            else:
                result = 'Gana ' + name_teamB
                
            self.result_dialog.format_secondary_text(result)
            self.result_dialog.run()
