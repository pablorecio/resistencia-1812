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

import gtk

from resistencia import configure, filenames, xdg

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

        self.teams[name] = (rules_file_name, formation_file_name)

        self.list_store.append((name, rules_file_name, formation_file_name))
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
        
        self.sName = "Name"
        self.sRules = "Rules"
        self.sFormation = "Formation"
        
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

        self.radio_league = builder.get_object('radio_league')
        self.radio_cup = builder.get_object('radio_cup')
        self.radio_groups = builder.get_object('radio_groups')

        self.check_backround = builder.get_object('check_backround')
        
        def_path = configure.load_configuration()['se_path']
        self.file_chooser_rules.set_current_folder(def_path + '/rules')
        self.file_chooser_formation.set_current_folder(def_path + '/formations')
        
        builder.connect_signals(self)

    def on_btn_add_clicked(self, widget, data=None):
        self.file_chooser_rules.connect('response', lambda d, r: d.hide())
        self.contest_dialog.hide()
        self.file_chooser_rules.show()
        
    def on_btn_remove_clicked(self, widget, data=None):
        del self.teams[self.list_store.get_value(self.treeiter, 0)]
        self.list_store.remove(self.treeiter)

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

    # ---- Radio button

    def on_radio_league_toggled(self, widget, data=None):
        if self.radio_league.get_active():
            self.check_backround.set_sensitive(True)
        else:
            self.check_backround.set_sensitive(False)

    def on_radio_cup_toggled(self, widget, data=None):
        print 'Copa toggled'

    def on_radio_groups_toggled(self, widget, data=None):
        print 'Round toggled'
        
