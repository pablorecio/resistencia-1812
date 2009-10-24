import sys
import gtk

class settingsDialog:
    def __init__(self, parent):
        builder = gtk.Builder()
        builder.add_from_file("./gui/glade/settingsDialog.glade")

        self.settings = builder.get_object("settingsDialog")
        self.settings.set_transient_for(parent)
        builder.connect_signals(self)
        
    def on_settingsDialog_close(self, widget, data=None):
        self.settings.hide()

    def on_btn_cancel_clicked(self, widget, data=None):
        self.settings.hide()
