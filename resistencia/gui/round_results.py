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

import sys
sys.path.append('../../')

import gtk

from resistencia import xdg
from resistencia.nls import gettext as _

class roundResults:
    def add_column(self, list_view, title, columnId):
        column = gtk.TreeViewColumn(title, gtk.CellRendererText(), markup=columnId)
        list_view.append_column(column)

    def fill_classification(self):
        i = 1
        print self.classifications
        for e in self.classifications:
            self.list_store_classifications.append((i, e[0], e[1]))
            i = i + 1

    def fill_results(self):
        for e in self.results:
            teamA = e[0][0];
            teamB = e[0][1];
            win_color = '#0C0C9D'
            draw_color = '#5DEA5D'
            if e[1] == 1:
                teamA = '<span foreground="' + win_color + '"><b>' + teamA + '</b></span>'
            elif e[1] == -1:
                teamB = '<span foreground="' + win_color + '"><b>' + teamB + '</b></span>'
            else: #draw
                teamA = '<span foreground="' + draw_color + '"><b>' + teamA + '</b></span>'
                teamB = '<span foreground="' + draw_color + '"><b>' + teamB + '</b></span>'
            self.list_store_results.append((teamA, teamB))
    
    def __init__(self, classification, results, round, rounds): #add parent
        builder = gtk.Builder()
        builder.add_from_file(xdg.get_data_path('glade/results.glade'))

        self.classifications = classification
        self.results = results
        self.round = round
        self.rounds = rounds

        self.result_dialog = builder.get_object('dlg_results')
        title = self.result_dialog.get_title()  + ' ' + str(round) + '/' + str(rounds)
        self.result_dialog.set_title(title)
        self.confirmation_dialog = builder.get_object('dlg_confirmation_close')
        self.confirmation_dialog.connect('response', lambda d, r: d.hide())
        self.confirmation_dialog.set_transient_for(self.result_dialog)
        self.finalround_dialog = builder.get_object('dlg_finalround')
        self.finalround_dialog.connect('response', lambda d, r: d.hide())
        self.finalround_dialog.set_transient_for(self.result_dialog)

        self.list_view_classifications = builder.get_object('treeview_classification')
        self.list_view_results = builder.get_object('treeview_results')

        self.cPosition = 0
        self.cTeamName = 1
        self.cPuntuations = 2
        
        self.sPosition = 'Pos'
        self.sTeamName = _('Team name')
        self.sPuntuations = 'Punt'

        self.add_column(self.list_view_classifications,
                        self.sPosition, self.cPosition)
        self.add_column(self.list_view_classifications,
                        self.sTeamName, self.cTeamName)
        self.add_column(self.list_view_classifications,
                        self.sPuntuations, self.cPuntuations)

        self.list_store_classifications = builder.get_object('list_classification')
        self.fill_classification()

        self.cTeamA = 0
        self.cTeamB = 1

        self.sTeamA = _('Team A')
        self.sTeamB = _('Team B')

        self.add_column(self.list_view_results, self.sTeamA, self.cTeamA)
        self.add_column(self.list_view_results, self.sTeamB, self.cTeamB)

        self.list_store_results = builder.get_object('list_results')
        self.fill_results()

        self.end_contest = False
        
        builder.connect_signals(self)

    def on_dlg_results_show(self, data=None):
        print 'on_dlg_results_show'
        if self.round == self.rounds:
            self.finalround_dialog.run()

    def on_btn_results_cancel_clicked(self, widget):
        self.confirmation_dialog.run()

    def on_btn_results_next_clicked(self, widget):
        self.result_dialog.hide()

    def on_dlg_results_close(self, widget, data=None):
        self.result_dialog.destroy()

    def on_btn_confirmation_apply_clicked(self, widget, data=None):
        self.confirmation_dialog.destroy()
        self.result_dialog.destroy()
        self.end_contest = True

    def on_btn_confirmation_cancel_clicked(self, widget, data=None):
        self.confirmation_dialog.hide()
        self.result_dialog.run()
        
