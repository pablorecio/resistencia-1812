import os
import sys
sys.path.append("..")

import gtk

import configure

class settingsDialog:
    def __init__(self, parent):
        builder = gtk.Builder()
        builder.add_from_file("./gui/glade/settingsDialog.glade")

        self.settings = builder.get_object("settingsDialog")
        self.settings.set_transient_for(parent)

        self.file_chooser_games = builder.get_object("file_chs_prev_games")
        self.file_chooser_teams = builder.get_object("file_chs_se")

        config_vars = configure.load_configuration()

        games_current_folder = config_vars['games_path'] + '..'
        teams_current_folder = config_vars['se_path'] + '..'
        
        self.file_chooser_games.set_current_folder(games_current_folder)
        self.file_chooser_games.set_filename(config_vars['games_path'])
        self.file_chooser_teams.set_current_folder(teams_current_folder)
        self.file_chooser_teams.set_filename(config_vars['se_path'])
        
        builder.connect_signals(self)
        
    def on_settingsDialog_close(self, widget, data=None):
        self.settings.hide()

    def on_btn_cancel_clicked(self, widget, data=None):
        self.settings.hide()

    def on_btn_apply_clicked(self, widget, data=None):
        config_vars = configure.load_configuration()
        #current_games_path = self.file_chooser_games.get_current_folder()
        #current_teams_path = self.file_chooser_teams.get_current_folder()
        
        current_games_path = self.file_chooser_games.get_filename()
        current_teams_path = self.file_chooser_teams.get_filename()
        
        if current_games_path != config_vars['games_path']:
            configure.set_games_path(current_games_path)
        if current_teams_path != config_vars['se_path']:
            configure.set_se_path(current_teams_path)

        self.settings.hide()
