#!/usr/bin/python

import sys
sys.path.append("./gui")

import gtk
import gtk.glade
import locale
import gettext

import main_window
import configure

configure.load_configuration()

APP = 'resistencia'
DIR = 'po'

gettext.textdomain(APP)
gettext.bindtextdomain(APP, DIR)
gtk.glade.textdomain(APP)
gtk.glade.bindtextdomain(APP, DIR)
_ = gettext.gettext

  
def main():
    "Main function"
    editor = main_window.Resistencia()
    editor.window.show()
    print _("Loading main window")
    gtk.main()
    
if __name__ == "__main__":
    main()
