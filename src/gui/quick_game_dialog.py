import sys
import os.path
import gtk
sys.path.append("../guada-board")
sys.path.append("./guada-board")
import guada_board

class quickGameDialog:
    def __init__(self, parent):
        builder = gtk.Builder()
        builder.add_from_file("./gui/glade/quickGame.glade")

        def_path = os.path.realpath('./teams')
        print def_path
        builder.get_object('file_chooser_es_a').set_current_folder(def_path)
        builder.get_object('file_chooser_team_a').set_current_folder(def_path)
        builder.get_object('file_chooser_es_b').set_current_folder(def_path)
        builder.get_object('file_chooser_team_b').set_current_folder(def_path)

        self.quick_game = builder.get_object("quickGameDialog")
        self.quick_game.set_transient_for(parent)
        builder.connect_signals(self)
        
    def on_quickGameDialog_close(self, widget, data=None):
        self.quick_game.hide()

    def on_file_chooser_es_a_file_set(self, widget, data=None):
        self.es_team_a = widget.get_uri()

    def on_file_chooser_team_a_file_set(self, widget, data=None):
        self.team_team_a = widget.get_uri()
        
    def on_file_chooser_es_b_file_set(self, widget, data=None):
        self.es_team_b = widget.get_uri()

    def on_file_chooser_team_b_file_set(self, widget, data=None):
        self.team_team_b = widget.get_uri()

    def on_btn_cancel_clicked(self, widget, data=None):
        self.quick_game.hide()

    def on_btn_apply_clicked(self, widget, data=None):        
        try: self.es_team_a
        except NameError:
            print 'No has inicializado el SE A'
        else:
            self.es_team_a = self.es_team_a[7:]
            print self.es_team_a
            
        try: self.es_team_b
        except NameError:
            print 'No has inicializado el SE B'
        else:
            self.es_team_b = self.es_team_b[7:]
            print self.es_team_b
            
        try: self.team_team_a
        except NameError:
            print 'No has inicializado el SE A'
        else:
            self.team_team_a = self.team_team_a[7:]
            print self.team_team_a
            
        try: self.team_team_b
        except NameError:
            print 'No has inicializado el SE B'
        else:
            self.team_team_b = self.team_team_b[7:]
            print self.team_team_b

        guada_board.run((self.es_team_a,self.team_team_a),
                        (self.es_team_b,self.team_team_b))
