import sys
import gtk
import gtk.glade
import settings_dialog
import quick_game_dialog

import configure
sys.path.append("./guada-board")
import guada_board

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

    def on_btn_previous_games_clicked(self, widget):
        self.previous_games_chooser.connect('response', lambda d, r: d.hide())
                                            #self.previous_games_file_chooser_handler)
        self.previous_games_chooser.set_transient_for(self.window)
        self.previous_games_chooser.show()

    def on_btn_settings_clicked(self, widget):
        settings_dial = settings_dialog.settingsDialog(self.window)
        settings_dial.settings.run()

    def on_btn_quick_game_clicked(self, widget):
        quick_game = quick_game_dialog.quickGameDialog(self.window)
        quick_game.quick_game.run()

    def on_btn_file_chooser_apply_clicked(self, widget):
        self.previous_games_file_chooser_handler():
        self.previous_games_chooser.hide()

    def on_btn_file_chooser_close_clicked(self, widget):
        self.previous_games_chooser.hide()
        
    def __init__(self):
        "Constructor of the object"
        builder = gtk.Builder()
        builder.add_from_file("./gui/glade/main.glade") 
        
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
