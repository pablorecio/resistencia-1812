import sys
import gtk
import gtk.glade
import settings_dialog
import quick_game_dialog

class Resistencia:
    """
    @brief Main class of the application 'Resistencia en Cadiz: 1812'.

    This class allows to start the program, and connect all events of the
    main window
    """
    def on_mainWindow_destroy(self, widget, data=None):
        gtk.main_quit()

    def on_btn_quit_clicked(self, widget, data=None):
        gtk.main_quit()

    def on_btn_about_clicked(self, widget):
        self.about.connect('response', lambda d, r: d.hide())
        self.about.set_transient_for(self.window)
        self.about.show()

    def on_btn_settings_clicked(self, widget):
        settings_dial = settings_dialog.settingsDialog(self.window)
        settings_dial.settings.run()

    def on_btn_quick_game_clicked(self, widget):
        quick_game = quick_game_dialog.quickGameDialog(self.window)
        quick_game.quick_game.run()
        
    def __init__(self):
        "Constructor of the object"
        builder = gtk.Builder()
        builder.add_from_file("./gui/glade/main.glade") 
        
        self.window = builder.get_object("mainWindow")
        self.about = builder.get_object("aboutdialog1")
        builder.connect_signals(self)
