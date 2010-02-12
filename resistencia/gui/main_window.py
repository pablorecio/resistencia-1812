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

import gtk
import gtk.glade

from guadaboard import guada_board
from resistencia import configure, xdg

import settings_dialog
import quick_game_dialog
import contest_dialog
import tests_dialog
import human_game_dialog

class Resistencia:
    """
    @brief Main class of the application 'Resistencia en Cadiz: 1812'.

    This class allows to start the program, and connect all events of the
    main window
    """
    def previous_games_file_chooser_handler(self):
        selected_file = self.previous_games_chooser.get_filename()
        if not (selected_file == None):
            print 'Seleccionado ' + selected_file
            guada_board.run_from_file(selected_file)
            return True
        else:
            self.games_chooser_warning.show()
            return False
    
    def on_mainWindow_destroy(self, widget, data=None):
        gtk.main_quit()

    def on_btn_quit_clicked(self, widget, data=None):
        gtk.main_quit()

    def on_btn_about_clicked(self, widget):
        self.about.connect('response', lambda d, r: d.hide())
        self.about.set_transient_for(self.window)
        self.about.show()

    def on_btn_competitions_clicked(self, widget):
        treeview = contest_dialog.contestDialog(self.window)
        treeview.contest_dialog.run()

    def on_btn_human_es_game_clicked(self, widget):
        human_es_game = human_game_dialog.humanGameDialog(self.window)
        human_es_game.human_ia_dialog.run()

    def on_btn_previous_games_clicked(self, widget):
        self.previous_games_chooser.connect('response', lambda d, r: d.hide())
                                            #self.previous_games_file_chooser_handler)
        self.previous_games_chooser.set_transient_for(self.window)
        self.previous_games_chooser.show()

    def on_btn_laboratory_clicked(self, widget):
        testing_dialog = tests_dialog.testDialog(self.window)
        testing_dialog.tests_dialog.run()

    def on_btn_settings_clicked(self, widget):
        settings_dial = settings_dialog.settingsDialog(self.window)
        settings_dial.settings.run()

    def on_btn_quick_game_clicked(self, widget):
        quick_game = quick_game_dialog.quickGameDialog(self.window)
        quick_game.quick_game.run()

    def on_btn_file_chooser_apply_clicked(self, widget):
        self.previous_games_file_chooser_handler()
        self.previous_games_chooser.hide()

    def on_btn_file_chooser_close_clicked(self, widget):
        self.previous_games_chooser.hide()
        
    def __init__(self):
        "Constructor of the object"
        builder = gtk.Builder()
        builder.add_from_file(xdg.get_data_path('glade/main.glade')) 
        
        self.window = builder.get_object("mainWindow")
        self.about = builder.get_object("aboutdialog1")
        self.previous_games_chooser = builder.get_object("filechooserdialog1")
        self.games_chooser_warning = builder.get_object("messagedialog1")

        
        self.games_chooser_warning.connect('response', lambda d, r: d.hide())
        self.games_chooser_warning.set_transient_for(self.previous_games_chooser)

        self.previous_games_chooser.set_transient_for(self.window)
        self.about.set_transient_for(self.window)
        
        def_path = configure.load_configuration()['games_path']
        self.previous_games_chooser.set_current_folder(def_path)
        builder.connect_signals(self)
