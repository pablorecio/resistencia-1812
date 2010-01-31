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
        column = gtk.TreeViewColumn(title, gtk.CellRendererText(),
                                    text=columnId)
        list_view.append_column(column)

    def fill_classification(self):
        i = 1
        print self.classifications
        for e in self.classifications:
            self.list_store_classifications.append((i, e[0], e[1]))
            i = i + 1

    def fill_results(self):
        for e in self.results:
            self.list_store_results.append((e[0][0], e[0][1], e[1]))
    
    def __init__(self, classification, results): #add parent
        builder = gtk.Builder()
        builder.add_from_file(xdg.get_data_path('glade/results.glade'))

        self.classifications = classification
        self.results = results

        self.result_dialog = builder.get_object('dlg_results')
        self.confirmation_dialog = builder.get_object('dlg_confirmation_close')
        self.confirmation_dialog.connect('response', lambda d, r: d.hide())
        self.confirmation_dialog.set_transient_for(self.result_dialog)

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
        self.cResult = 2

        self.sTeamA = _('Team A')
        self.sTeamB = _('Team B')
        self.sResult = _('Result')

        self.add_column(self.list_view_results, self.sTeamA, self.cTeamA)
        self.add_column(self.list_view_results, self.sTeamB, self.cTeamB)
        self.add_column(self.list_view_results, self.sResult, self.cResult)

        self.list_store_results = builder.get_object('list_results')
        self.fill_results()

        self.end_contest = False
        
        builder.connect_signals(self)

    def on_btn_results_cancel_clicked(self, widget):
        self.confirmation_dialog.show()

    def on_btn_results_next_clicked(self, widget):
        print 'Pulsado 1'
        self.result_dialog.hide()
        print 'Pulsado 2'

    def on_dlg_results_close(self, widget, data=None):
        self.result_dialog.destroy()

    def on_btn_confirmation_apply_clicked(self, widget, data=None):
        self.confirmation_dialog.destroy()
        self.result_dialog.destroy()
        self.end_contest = True

    def on_btn_confirmation_cancel_clicked(self, widget, data=None):
        self.confirmation_dialog.hide()
