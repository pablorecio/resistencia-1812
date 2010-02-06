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
import os.path

import gtk

from resistencia import filenames, xdg
from resistencia.nls import gettext as _

class notifyResult:
    def __init__(self, teams, winner):
        name_teamA = teams[0]
        name_teamB = teams[1]
        
        result = ''
        
        if winner == 0:
            result = _('Draw')
        elif winner == 1:
            result = _('Wins ') + name_teamA
        else:
            result = _('Gana ') + name_teamB
            
        builder = gtk.Builder()
        builder.add_from_file(xdg.get_data_path('glade/resultNotifier.glade'))

        self.dlg_result = builder.get_object('dlg_result')
        self.dlg_result.connect('response', lambda d, r: d.hide())
        self.dlg_result.format_secondary_text(result)
