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
from resistencia.contest import league

class playersSelection(object):
    # ------- First, auxiliary functions, not associated with events
    def add_column(self, title, columnId):
        column = gtk.TreeViewColumn(title, gtk.CellRendererText(),
                                    text=columnId)

        column.set_resizable(False)
        column.set_clickable(False)
        column.set_reorderable(False)

        column.set_sort_column_id(columnId)
        self.list_view.append_column(column)

    def insert_element_list(self):
        s, rules_file_name = os.path.split(self.rules_selected_file)
        s, formation_file_name = os.path.split(self.formation_selected_file)
        self.files[rules_file_name] = self.rules_selected_file
        self.files[formation_file_name] = self.formation_selected_file

        name = filenames.extract_name_expert_system((rules_file_name,
                                                     formation_file_name))

        self.teams[name] = (rules_file_name, formation_file_name)

        self.list_store.append((name, rules_file_name, formation_file_name))

    # ------- File chooser's dialogs handlers
    def file_chooser_rules_handler(self):
        self.rules_selected_file = self.file_chooser_rules.get_filename()
        assert(not(self.rules_selected_file == None))

    def file_chooser_formation_handler(self):
        self.formation_selected_file = self.file_chooser_formation.get_filename()
        assert(not(self.formation_selected_file == None))

    # ------- Events handlers

    def on_list_es_view_cursor_changed(self, widget, data=None):
        self.treeiter = self.list_store.get_iter(widget.get_cursor()[0])

    def on_btn_add_clicked(self, widget, data=None):
        self.file_chooser_rules.connect('response', lambda d, r: d.hide())
        self.players_selector.hide()
        self.file_chooser_rules.show()

    def on_btn_remove_clicked(self, widget, data=None):
        del self.teams[self.list_store.get_value(self.treeiter, 0)]
        self.list_store.remove(self.treeiter)

    def on_players_selector_close(self, widget, data=None):
        self.players_selector.hide()

    def on_btn_cancel_clicked(self, widget, data=None):
        self.players_selector.hide()

    def on_btn_apply_clicked(self, widget, data=None):
        l = league.League(self.teams)
        l.play_round()
        self.players_selector.hide()

    # ---- Event handlers for file chooser dialogs
    def on_btn_file_chooser_rules_apply_clicked(self, widget):
        self.file_chooser_rules_handler()
        self.file_chooser_rules.hide()
        self.file_chooser_formation.show()

    def on_btn_file_chooser_rules_close_clicked(self, widget):
        self.file_chooser_rules.hide()
        self.players_selector.show()
        del self.rules_selected_file

    def on_btn_file_chooser_formation_apply_clicked(self, widget):
        self.file_chooser_formation_handler()
        self.file_chooser_formation.hide()
        self.players_selector.show()
        self.insert_element_list()

    def on_btn_file_chooser_formation_close_clicked(self, widget):
        self.file_chooser_formation.hide()
        del self.rules_selected_file
        del self.formation_selected_file

    # ---- Initialization

    def __init__ (self, parent):
        builder = gtk.Builder()
        builder.add_from_file(xdg.get_data_path('glade/tree.glade'))

        self.players_selector = builder.get_object('players_selector')
        self.players_selector.set_transient_for(parent)

        self.files = {}
        self.teams = {}

        # ---- Building the table
        self.cName = 0
        self.cRules = 1
        self.cFormation = 2

        self.sName = 'Name'
        self.sRules = 'Rules'
        self.sFormation = 'Formation'
        
        self.list_view = builder.get_object("list_es_view")
        self.list_view.set_reorderable(False)

        self.add_column(self.sName, self.cName)
        self.add_column(self.sRules, self.cRules)
        self.add_column(self.sFormation, self.cFormation)

        self.list_store = builder.get_object('list_expert_system')
        # -----
        
        self.file_chooser_rules = builder.get_object('file_chooser_rules')
        self.file_chooser_formation = builder.get_object('file_chooser_formation')
        
        def_path = configure.load_configuration()['se_path']
        self.file_chooser_rules.set_current_folder(def_path + '/rules')
        self.file_chooser_formation.set_current_folder(def_path + '/formations')
        
        builder.connect_signals(self)
