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

import gtk

from guadaboard import guada_board
from resistencia import configure, xdg, filenames

class testDialog:
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
        self.file_chooser_formation.run()

    def apply_file_chooser_formation(self):
        self.file_chooser_formation_handler()
        self.file_chooser_formation.hide()
        #self.tests_dialog.show()
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
        self.rules_main_team = ''
        self.formation_main_team = ''
        self.files = {}
        self.teams = {}

        builder = gtk.Builder()
        builder.add_from_file(xdg.get_data_path('glade/testDialog.glade'))

        self.tests_dialog = builder.get_object('tests_dialog')
        self.tests_dialog.set_transient_for(parent)

        # ---- Init file chooser buttons
        default_path = configure.load_configuration()['se_path']
        default_rules_path = default_path + '/rules'
        default_formations_path = default_path + '/formations'
        builder.get_object('btn_filechooser_rules').set_current_folder(default_rules_path)
        builder.get_object('btn_filechooser_formation').set_current_folder(default_formations_path)
        # ----

        self.num_rounds = 2
        self.spin_rounds = builder.get_object('spin_rounds')
        self.spin_rounds.set_range(2, 100)
        self.spin_rounds.set_increments(2,10)
        self.spin_rounds.set_value(self.num_rounds)

        self.all_teams = False
        self.frame_selection_teams = builder.get_object('frame_es_selection')

        self.start_button = builder.get_object('btn_apply')
        self.start_button.set_sensitive(False)
        
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
        self.file_chooser_formation = builder.get_object('file_chooser_formation')
        self.file_chooser_rules.set_current_folder(default_rules_path)
        self.file_chooser_formation.set_current_folder(default_formations_path)
        
        builder.connect_signals(self)
    
    def on_tests_dialog_close(self, widget, data=None):
        """
        Function that handles the closing event of the dialog
        """
        self.tests_dialog.hide()

    def on_btn_filechooser_rules_file_set(self, widget, data=None):
        self.rules_main_team = widget.get_uri()
    
    def on_btn_filechooser_formation_file_set(self, widget, data=None):
        self.formation_main_team = widget.get_uri()

    def on_spin_rounds_change_value(self, widget, data=None):
        self.num_rounds = widget.get_value()

    def on_spin_rounds_value_changed(self, widget, data=None):
        self.num_rounds = widget.get_value()

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
            

    def on_list_es_view_cursor_changed(self, widget, data=None):
        self.treeiter = self.list_store.get_iter(widget.get_cursor()[0])        

    def on_btn_add_clicked(self, widget, data=None):
        self.file_chooser_rules.connect('response', lambda d, r: d.hide())
        #self.tests_dialog.hide()
        self.file_chooser_rules.run()
        
    def on_btn_remove_clicked(self, widget, data=None):
        del self.teams[self.list_store.get_value(self.treeiter, 0)]
        self.list_store.remove(self.treeiter)
        if len(self.teams) == 1:
            self.start_button.set_sensitive(False)
    
    def on_btn_file_chooser_rules_apply_clicked(self, widget):
        self.apply_file_chooser_rules()

    def on_file_chooser_rules_file_activated(self, widget):
        self.apply_file_chooser_rules()

    def on_btn_file_chooser_rules_close_clicked(self, widget):
        self.file_chooser_rules.hide()
        self.tests_dialog.show()
        del self.rules_selected_file

    def on_btn_file_chooser_formation_apply_clicked(self, widget):
        self.apply_file_chooser_formation()

    def on_file_chooser_formation_file_activated(self, widget):
        self.apply_file_chooser_formation()

    def on_btn_file_chooser_formation_close_clicked(self, widget):
        self.file_chooser_formation.hide()
        del self.rules_selected_file
        del self.formation_selected_file

    def on_btn_apply_clicked(self, widget, data=None):
        print self.teams
        print self.files
        print self.num_rounds
        
    def on_btn_cancel_clicked(self, widget, data=None):
        self.tests_dialog.hide()
        

    
