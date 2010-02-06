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

import os
import os.path

import gtk

from resistencia import xdg
import piechart

class testResult:
    def __init__(self, stats, team):
        self.output_file = 'tmp.png'
        line = []
        if not stats['wins'] == 0:
            line.append(('wins', stats['wins']))
        if not stats['draws'] == 0:
            line.append(('draws', stats['draws']))
        if not stats['looses'] == 0:
            line.append(('looses', stats['looses']))

        piechart.pieChart(self.output_file, line)
        
        builder = gtk.Builder()
        builder.add_from_file(xdg.get_data_path('glade/testResults.glade'))

        self.test_result = builder.get_object('test_result_dialog')
        self.test_result.set_title(self.test_result.get_title().replace('@team@',
                                                                        team))
        #self.tests_dialog.set_transient_for(parent)

        builder.get_object('pie_chart').set_from_file(self.output_file)

        num_games = stats['wins'] + stats['draws'] + stats['looses']
        wins = stats['wins']
        draws = stats['draws']
        looses = stats['looses']
        try:
            turns_winning = stats['turns_winning'] / wins
        except ZeroDivisionError:
            turns_winning = 0

        try:
            turns_loosing = stats['turns_losing'] / looses
        except ZeroDivisionError:
            turns_loosing = 0
            
        num_pieces = stats['num_pieces'] / num_games
        val_pieces = stats['val_pieces'] / num_games
        max_death = stats['max_death'] / num_games

        text = builder.get_object('lbl_num_games').get_label()
        builder.get_object('lbl_num_games').set_label(text.replace('@value@', str(num_games)))
        text = builder.get_object('lbl_wins').get_label()
        builder.get_object('lbl_wins').set_label(text.replace('@value@', str(wins)))
        text = builder.get_object('lbl_draws').get_label()
        builder.get_object('lbl_draws').set_label(text.replace('@value@', str(draws)))
        text = builder.get_object('lbl_looses').get_label()
        builder.get_object('lbl_looses').set_label(text.replace('@value@', str(looses)))
        text = builder.get_object('lbl_turns_win').get_label()
        builder.get_object('lbl_turns_win').set_label(text.replace('@value@', str(turns_winning)))
        text = builder.get_object('lbl_turns_lose').get_label()
        builder.get_object('lbl_turns_lose').set_label(text.replace('@value@', str(turns_loosing)))
        text = builder.get_object('lbl_max_piece').get_label()
        builder.get_object('lbl_max_piece').set_label(text.replace('@value@', str(max_death)))

        builder.connect_signals(self)                

    def on_test_result_dialog_close(self, widget, data=None):
        self.test_result.destroy()
        os.remove(self.output_file)

    def on_btn_apply_clicked(self, widget, data=None):
        self.test_result.destroy()
        os.remove(self.output_file)
        

