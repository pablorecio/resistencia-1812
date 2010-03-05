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

import os
import sys
import types

import gtk

from resistencia import configure, filenames, xdg
from resistencia.contest import main as contest
from resistencia.tests import selection
from resistencia.nls import gettext as _
import tests_result

class contestDialog:
    # --- List and handler functions
    def addColumn(self, title, columnId):	
        column = gtk.TreeViewColumn(title, gtk.CellRendererText(),
                                    text=columnId)
        self.list_view.append_column(column)

    def file_chooser_rules_handler(self):
        self.rules_selected_file = self.file_chooser_rules.get_filename()
        assert(not(self.rules_selected_file == None))

    def file_chooser_formation_handler(self):
        self.formation_selected_file = self.file_chooser_formation.get_filename()
        assert(not(self.formation_selected_file == None))

    def apply_file_chooser_rules(self):
        self.file_chooser_rules_handler()
        self.file_chooser_rules.hide()
        self.file_chooser_formation.show()

    def apply_file_chooser_formation(self):
        self.file_chooser_formation_handler()
        self.file_chooser_formation.hide()
        self.contest_dialog.show()
        self.insert_element_list()

    def insert_element_list(self):
        s, rules_file_name = os.path.split(self.rules_selected_file)
        s, formation_file_name = os.path.split(self.formation_selected_file)
        self.files[rules_file_name] = self.rules_selected_file
        self.files[formation_file_name] = self.formation_selected_file

        name = filenames.extract_name_expert_system((rules_file_name,
                                                     formation_file_name))

        if not self.teams.has_key(name):
            self.teams[name] = (self.rules_selected_file, self.formation_selected_file)

            self.list_store.append((name, rules_file_name, formation_file_name))
            if len(self.teams) == 2:
                self.start_button.set_sensitive(True)
    # ---
    def __init__(self, parent):
        builder = gtk.Builder()
        builder.add_from_file(xdg.get_data_path('glade/contest.glade'))
        
        self.contest_dialog = builder.get_object("contest_dialog")
        self.contest_dialog.set_transient_for(parent)

        self.files = {}
        self.teams = {}

        #---------------------------
        self.cName = 0
        self.cRules = 1
        self.cFormation = 2
        
        self.sName = _("Name")
        self.sRules = _("Rules")
        self.sFormation = _("Formation")
        
        self.list_view = builder.get_object("list_es_view")
        self.list_view.set_reorderable(False)

        self.addColumn(self.sName, self.cName)
        self.addColumn(self.sRules, self.cRules)
        self.addColumn(self.sFormation, self.cFormation)

        self.list_store = builder.get_object("list_expert_system")
        #-----------------------------

        self.file_chooser_rules = builder.get_object('file_chooser_rules')
        #self.file_chooser_rules.set_transient_for(self.players_selector)
        self.file_chooser_formation = builder.get_object('file_chooser_formation')
        #self.file_chooser_formation.set_transient_for(self.players_selector)

        self.format_contest = 'league'
        self.radio_league = builder.get_object('radio_league')
        self.radio_cup = builder.get_object('radio_cup')
        self.radio_groups = builder.get_object('radio_groups')
        self.radio_playoff = builder.get_object('radio_playoff')
        self.check_backround = builder.get_object('check_backround')
        self.check_fast = builder.get_object('check_onlyresults')

        self.back_round = False
        self.fast = False
        self.all_teams = False
        
        def_path = configure.load_configuration()['se_path']
        self.file_chooser_rules.set_current_folder(def_path + '/rules')
        self.file_chooser_formation.set_current_folder(def_path + '/formations')

        self.start_button = builder.get_object('btn_start')
        self.frame_selection_teams = builder.get_object('box_selection')
        
        self.num_turns = 120
        self.spin_turns = builder.get_object("spin_num_turns")
        self.spin_turns.set_range(50,300)
        self.spin_turns.set_increments(2,10)
        self.spin_turns.set_value(self.num_turns)
        
        builder.connect_signals(self)

    def on_btn_add_clicked(self, widget, data=None):
        self.file_chooser_rules.connect('response', lambda d, r: d.hide())
        self.contest_dialog.hide()
        self.file_chooser_rules.show()
        
    def on_btn_remove_clicked(self, widget, data=None):
        del self.teams[self.list_store.get_value(self.treeiter, 0)]
        self.list_store.remove(self.treeiter)
        if len(self.teams) == 1:
            self.start_button.set_sensitive(False)

    def on_list_es_view_cursor_changed(self, widget, data=None):
        self.treeiter = self.list_store.get_iter(widget.get_cursor()[0])

    def on_contest_diaog_close(self, widget, data=None):
        self.contest_dialog.hide()

    def on_btn_file_chooser_rules_apply_clicked(self, widget):
        self.apply_file_chooser_rules()

    def on_file_chooser_rules_file_activated(self, widget):
        self.apply_file_chooser_rules()

    def on_btn_file_chooser_rules_close_clicked(self, widget):
        self.file_chooser_rules.hide()
        self.contest_dialog.show()
        del self.rules_selected_file

    def on_btn_file_chooser_formation_apply_clicked(self, widget):
        self.apply_file_chooser_formation()

    def on_file_chooser_formation_file_activated(self, widget):
        self.apply_file_chooser_formation()

    def on_btn_file_chooser_formation_close_clicked(self, widget):
        self.file_chooser_formation.hide()
        del self.rules_selected_file
        del self.formation_selected_file

    def on_btn_cancel_clicked(self, widget, data=None):
        self.contest_dialog.hide()

    def on_btn_start_clicked(self, widget, data=None):
        if self.all_teams:
            self.teams = selection.get_installed_teams()
        self.contest_dialog.destroy()
        while gtk.events_pending():
            gtk.main_iteration(False)
        contest.init_contest(self.format_contest, self.teams,
                             self.fast, self.back_round, self.num_turns)

    # ---- Radio button

    def on_radio_league_toggled(self, widget, data=None):
        if self.radio_league.get_active():
            self.check_backround.set_sensitive(True)
            self.format_contest = 'league'
        else:
            self.check_backround.set_sensitive(False)

    def on_radio_cup_toggled(self, widget, data=None):
        if self.radio_cup.get_active():
            self.format_contest = 'cup'

    def on_radio_groups_toggled(self, widget, data=None):
        if self.radio_group.get_active():
            self.format_contest = 'group'
            
    def on_radio_playoff_toggled(self, widget, data=None):
        if self.radio_playoff.get_active():
            self.check_backround.set_sensitive(True)
            self.format_contest = 'playoff'
        else:
            self.check_backround.set_sensitive(False)

    def on_check_backround_toggled(self, widget, data=None):
        print 'hola'
        if self.check_backround.get_active():
            self.back_round = True
        else:
            self.back_round = False

    def on_check_onlyresults_toggled(self, widget, data=None):
        if self.check_fast.get_active():
            self.fast = True
        else:
            self.fast = False
    
    def on_check_all_teams_toggled(self, widget, data=None):
        self.all_teams = widget.get_active()
        if self.all_teams:
            self.frame_selection_teams.set_sensitive(False)
            self.start_button.set_sensitive(True)
        else:
            self.frame_selection_teams.set_sensitive(True)
            if len(self.teams) >= 2:
                self.start_button.set_sensitive(True)
            else:
                self.start_button.set_sensitive(False)

    def on_spin_num_turns_change_value(self, widget, data=None):
        self.num_turns = int(widget.get_value())

    def on_spin_num_turns_value_changed(self, widget, data=None):
        self.num_turns = int(widget.get_value())
        
