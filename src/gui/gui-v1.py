 #!/usr/bin/env python

import sys
import gtk
  
class Resistencia:
    def on_mainWindow_destroy(self, widget, data=None):
        gtk.main_quit()

    def on_btn_quit_clicked(self, widget, data=None):
        gtk.main_quit()
        
    def __init__(self):
        "Constructor of the object"
        builder = gtk.Builder()
        builder.add_from_file("v1.xml") 
        
        self.window = builder.get_object("mainWindow")
        builder.connect_signals(self)       
    
if __name__ == "__main__":
    "Main function"
    editor = Resistencia()
    editor.window.show() #this is gtk.gdk.window, not a gtk.window
    gtk.main()
