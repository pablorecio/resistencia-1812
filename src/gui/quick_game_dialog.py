import sys
import gtk

class quickGameDialog:
    def __init__(self, parent):
        builder = gtk.Builder()
        builder.add_from_file("quickGame.glade")

        self.quick_game = builder.get_object("quickGameDialog")
        self.quick_game.set_transient_for(parent)
        builder.connect_signals(self)
        
    def on_quickGameDialog_close(self, widget, data=None):
        self.quick_game.hide()

    def on_btn_cancel_clicked(self, widget, data=None):
        self.quick_game.hide()
