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
import gtk

from resistencia import configure, filenames, xdg
from resistencia.gui import round_results

import league
import tournament
import round

def init_contest(contest_format, teams, fast=False, back_round=False):
    if contest_format == 'league':
        _init_league(_clean_dictionary(teams), fast, back_round)
    elif contest_format == 'cup':
        _init_tournament(_clean_dictionary(teams), fast)

def _init_league(teams, fast, back_round):    
    l = league.League(teams, back_round)

    band = False
    
    while not l.league_completed and not band:
        i = l.get_round_number()
        l.play_round(fast)
        r = l.get_round(i)
        
        classifications = l.get_actual_puntuations()
        results = r.get_round_results()
        
        R = round_results.roundResults(classifications, results, l.get_prev_round_number() + 1,
                                       l.get_number_of_rounds())
        button_pressed = R.result_dialog.run()
        
        while gtk.events_pending():
            gtk.main_iteration(False)
            
        if button_pressed == -4 or button_pressed == 0:
            band = True

def _init_tournament(teams, fast):
    t = tournament.Tournament(teams)
    band = False

    while not t.tournament_completed and not band:
        i = t.get_round_number()
        t.play_round(fast)
        r = t.get_round(i)

        classifications = []
        results = r.get_round_results()
        
        R = round_results.roundResults(classifications, results, t.get_prev_round_number() + 1,
                                       t.get_number_of_rounds(), show_classifications=False)

        button_pressed = R.result_dialog.run()
        
        while gtk.events_pending():
            gtk.main_iteration(False)
            
        if button_pressed == -4 or button_pressed == 0:
            band = True

def _clean_dictionary(d):
    l = []
    for k in d:
        l.append(d[k])

    return l
