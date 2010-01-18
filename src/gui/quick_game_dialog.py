import sys
import os.path
import gtk
sys.path.append("../guada-board")
sys.path.append("./guada-board")

import guada_board
import configure

class quickGameDialog:    
    def __init__(self, parent):
        self.es_team_a = ''
        self.team_team_a = ''
        self.es_team_b = ''
        self.team_team_b = ''
        
        builder = gtk.Builder()
        builder.add_from_file("./gui/glade/quickGame.glade")

        def_path = configure.load_configuration()['se_path']
        builder.get_object('file_chooser_es_a').set_current_folder(def_path)
        builder.get_object('file_chooser_team_a').set_current_folder(def_path)
        builder.get_object('file_chooser_es_b').set_current_folder(def_path)
        builder.get_object('file_chooser_team_b').set_current_folder(def_path)

        self.quick_game = builder.get_object("quickGameDialog")
        self.quick_game.set_transient_for(parent)
        #---- Initialation for the dialogs
        self.error_es_a = builder.get_object("error_no_es_a")
        self.error_es_a.connect('response', lambda d, r: d.hide())
        self.error_es_a.set_transient_for(self.quick_game)
        
        self.error_team_a = builder.get_object("error_no_team_a")
        self.error_team_a.connect('response', lambda d, r: d.hide())
        self.error_team_a.set_transient_for(self.quick_game)
        
        self.error_es_b = builder.get_object("error_no_es_b")
        self.error_es_b.connect('response', lambda d, r: d.hide())
        self.error_es_b.set_transient_for(self.quick_game)
        
        self.error_team_b = builder.get_object("error_no_team_b")
        self.error_team_b.connect('response', lambda d, r: d.hide())
        self.error_team_b.set_transient_for(self.quick_game)

        self.result_dialog = builder.get_object("dlg_result")
        self.result_dialog.connect('response', lambda d, r: d.hide())
        self.result_dialog.set_transient_for(self.quick_game)
        #---------------
        self.fast_game = False
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

    def on_check_fastgame_toggled(self, widget):
        self.fast_game = widget.get_active()

    def on_btn_cancel_clicked(self, widget, data=None):
        self.quick_game.hide()

    def on_btn_apply_clicked(self, widget, data=None):
        correct = True
        if len(self.es_team_a) == 0:
            self.error_es_a.show()
            correct = False
        else:
            self.es_team_a = self.es_team_a[7:]
            print self.es_team_a
            
        if len(self.es_team_b) == 0:
            self.error_es_b.show()
            correct = False
        else:
            self.es_team_b = self.es_team_b[7:]
            print self.es_team_b
            
        if len(self.team_team_a) == 0:
            self.error_team_a.show()
            correct = False
        else:
            self.team_team_a = self.team_team_a[7:]
            print self.team_team_a
            
        if len(self.team_team_b) == 0:
            self.error_team_b.show()
            correct = False
        else:
            self.team_team_b = self.team_team_b[7:]
            print self.team_team_b

        if correct == True:
            self.quick_game.hide()
            self.load_board()

    def load_board(self):
        winner = guada_board.run(((self.es_team_a,self.team_team_a), './images/piece-orange.png'),
                                 ((self.es_team_b,self.team_team_b), './images/piece-violete.png'),
                                 self.fast_game)
        if self.fast_game:
            result = ''
            if winner == 0:
                result = 'Empate'
            elif winner == 1:
                result = 'Gana ' + self.es_team_a
            else:
                result = 'Gana ' + self.es_team_b
                
            self.result_dialog.format_secondary_text(result)
            self.result_dialog.run()
