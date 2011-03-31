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

import gtk

from resistencia import xdg

class ProgressBarDialog:
    def __init__(self, parent, str_content):
        builder = gtk.Builder()
        progressbar_path = xdg.get_data_path('glade/progressbarDialog.glade')
        builder.add_from_file(progressbar_path)

        self.progress_bar_dialog = builder.get_object('progress_dialog')
        self.progress_bar_dialog.connect('response', lambda d, r: d.hide())
        self.progress_bar_dialog.set_transient_for(parent)

        lbl_content = builder.get_object('lbl_content')
        lbl_content.set_text(str_content)

        self.progress_bar = builder.get_object('progress_bar')

    def set_num_elements(self, num_elements):
        self.progress_bar.set_pulse_step(1 / float(num_elements))

    def pulse(self):
        self.progress_bar.pulse()
        pulse_step = self.progress_bar.get_pulse_step()
        frac = self.progress_bar.get_fraction() + pulse_step
        self.progress_bar.set_fraction(frac)
