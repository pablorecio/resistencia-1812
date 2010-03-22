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
import types

import gtk

from resistencia import configure, filenames, xdg
from resistencia.gui import round_results
from resistencia.gui import progress_bar_dialog as pbs

from resistencia.nls import gettext as _

import league
import contest
import tournament
import round

def init_contest(contest_format, teams, fast=False, back_round=False,
                 num_turns=120):
    if contest_format == 'league':
        _init_league(_clean_dictionary(teams), fast, num_turns, back_round)
    elif contest_format == 'cup':
        _init_tournament(_clean_dictionary(teams), num_turns, fast)
    elif contest_format == 'playoff':
        _init_playoff(_clean_dictionary(teams), fast, num_turns, back_round)
        

def _init_league(teams, fast, num_turns, back_round):
    l = league.League(teams, num_turns, back_round)

    band = False
    
    while not l.league_completed and not band:
        i = l.get_round_number()
        progress_bar = None
        if fast:
            progress_bar = pbs.ProgressBarDialog(None,
                                                 _('Running the contest'))
            progress_bar_dialog = progress_bar.progress_bar_dialog
            progress_bar.set_num_elements(l.get_round(i).number_games)
            progress_bar_dialog.show()
            while gtk.events_pending():
                gtk.main_iteration(False)
        l.play_round(progress_bar, fast)
        r = l.get_round(i)
        
        classifications = l.get_actual_puntuations()
        results = r.get_round_results()
        
        R = round_results.roundResults(classifications, results,
                                       l.get_prev_round_number() + 1,
                                       l.get_number_of_rounds())
        if fast:
            progress_bar_dialog.hide()
        button_pressed = R.result_dialog.run()
        
        while gtk.events_pending():
            gtk.main_iteration(False)
            
        if button_pressed == -4 or button_pressed == 0:
            band = True

def _init_tournament(teams, num_turns, fast):
    t = tournament.Tournament(teams, num_turns)
    band = False
    
    while not t.tournament_completed and not band:
        i = t.get_round_number()
        progress_bar = None
        if fast:
            progress_bar = pbs.ProgressBarDialog(None,
                                                 _('Running the contest'))
            progress_bar_dialog = progress_bar.progress_bar_dialog
            progress_bar.set_num_elements(t.get_round(i).number_games)
            progress_bar_dialog.show()
            while gtk.events_pending():
                gtk.main_iteration(False)
        t.play_round(progress_bar, fast)
        r = t.get_round(i)

        classifications = []
        results = r.get_round_results()
        
        R = round_results.roundResults(classifications, results,
                                       t.get_prev_round_number() + 1,
                                       t.get_number_of_rounds(),
                                       show_classifications=False)
        if fast:
            progress_bar_dialog.hide()
        button_pressed = R.result_dialog.run()
        
        while gtk.events_pending():
            gtk.main_iteration(False)
            
        if button_pressed == -4 or button_pressed == 0:
            band = True
    print teams


def _init_playoff(teams, fast, num_turns, back_round):
    l = league.League(teams, num_turns, back_round)

    band = False
    
    while not l.league_completed and not band:
        i = l.get_round_number()
        progress_bar = None
        if fast:
            progress_bar = pbs.ProgressBarDialog(None,
                                                 _('Running the contest'))
            progress_bar_dialog = progress_bar.progress_bar_dialog
            progress_bar.set_num_elements(l.get_round(i).number_games)
            progress_bar_dialog.show()
            while gtk.events_pending():
                gtk.main_iteration(False)
        l.play_round(progress_bar, fast)
        r = l.get_round(i)
        
        classifications = l.get_actual_puntuations()
        results = r.get_round_results()
        
        R = round_results.roundResults(classifications, results,
                                       l.get_prev_round_number() + 1,
                                       l.get_number_of_rounds(),
                                       show_top_teams=True)
        if fast:
            progress_bar_dialog.hide()
        button_pressed = R.result_dialog.run()
        
        while gtk.events_pending():
            gtk.main_iteration(False)
            
        if button_pressed == -4 or button_pressed == 0:
            band = True
    if not band:
        band = False
        teams = _get_teams_next_round(teams, _extract_classifications(classifications))
        _init_tournament(teams, num_turns, fast)
        


def _clean_dictionary(d):
    if type(d) == types.ListType:
        return d
    else:
        l = []
        for k in d:
            l.append(d[k])
            
        return l

def _get_teams_next_round(teams, classifications):
    translator = contest.generate_key_names(teams)

    teams_next_round = []
    n = len(teams) / 2

    for i in range(n):
        teams_next_round.append(translator[classifications[i]])

    return teams_next_round

def _extract_classifications(classifications):
    new_classifications = []
    for i in classifications:
        new_classifications.append(i[0])

    return new_classifications

    
        
