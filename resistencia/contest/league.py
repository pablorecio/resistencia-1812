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
import time

import os
import datetime
import random
import gtk

sys.path.append('../../')
from resistencia import configure, filenames, xdg
from resistencia.gui import round_results
import pairing
import round

def _generate_key_names(teams):
    d = {}

    for team in teams:
        name = filenames.extract_name_expert_system(team)
        d[name] = team

    return d

def _merge_puntuations(punt1, punt2):
    for index in punt1:
        punt1[index] = punt1[index] + punt2[index]

def _puntuations_compare(p1, p2):
    if p1[1] > p2[1]:
        return 1
    elif p1[1] == p2[1]:
        return 0
    else:
        return -1

class League(object):
    
    def __init__(self, teams, back_round=False):
        self.teams = teams
        self.translator = _generate_key_names(teams)
        self.keys = []

        for t in self.translator:
            self.keys.append(t)

        self.matchs = pairing.make_pairings(self.keys, back_round)

        self.rounds = []
        base_path = configure.load_configuration()['games_path'] + '/'
        self.tournament_file_name = base_path + filenames.generate_filename('tournament')
        print self.tournament_file_name
        
        for jorn in self.matchs:
            self.rounds.append(round.Round(jorn, self.translator,
                                           self.tournament_file_name))

        self.puntuations_by_round = []
        self.puntuations = {}
        for key in self.keys:
            self.puntuations[key] = 0

        self.number_of_rounds = len(self.rounds)
        self.actual_round = 0
        self.league_completed = False

    def get_round_number(self):
        return self.actual_round

    def get_round(self, round_number):
        return self.rounds[round_number]

    def play_round(self):
        if not self.league_completed:
            r = self.rounds[self.actual_round]
            n = r.get_number_of_games()

            for i in range(n):
                r.play_match()

            p = r.get_puntuation()
            self.puntuations_by_round.append(p)
            _merge_puntuations(self.puntuations, p)

            f_log = open(self.tournament_file_name, 'a')
            f_log.write('Ronda ' + str(self.actual_round+1) + ":\n")
            f_log.close()
            r.log_tournament(True)
            f_log = open(self.tournament_file_name, 'a')
            f_log.write('-------------------------------' + "\n")
            f_log.close()

            self.actual_round = self.actual_round + 1
            self.league_completed = (self.actual_round == self.number_of_rounds)

    def get_actual_puntuations(self):
        clasification = self.puntuations.items()
        clasification.sort(_puntuations_compare)
        clasification.reverse()

        return clasification

    def print_actual_puntuations(self):
        clasification = self.puntuations.items()
        clasification.sort(_puntuations_compare)
        clasification.reverse()

        for i in clasification:
            name = i[0]
            punt = i[1]

            if not name == 'aux_ghost_team':
                long_name = len(name)
                
                num_sep = 29 - long_name

                print name + ' ' + '-'*num_sep + ' ' + str(punt)
            

if __name__ == "__main__":

    rules = xdg.get_config_dir() + '/teams/rules'
    formations = xdg.get_config_dir() + '/teams/formations'
    teams = [(rules + '/reglasRafa.clp', formations + '/equipoRafa.clp'),
             (rules + '/reglasJavierS.clp', formations + '/equipoJavierS.clp'),
             (rules + '/reglasPabloRecio.clp',formations + '/equipoPabloRecio.clp'),
             (rules + '/reglasRosunix.clp', formations + '/equipoRosunix.clp')]#,
             #(rules + '/reglasGent0oza.clp', formations + '/equipoGent0oza.clp'),
             #(rules + '/reglasAbrahan.clp', formations + '/equipoAbrahan.clp'),
             #(rules + '/reglasPalomo.clp', formations + '/equipoPalomo.clp'),
             #(rules + '/reglasNoelia.clp', formations + '/equipoNoelia.clp')]

    l = League(teams, True)

    band = False

    while not l.league_completed and not band:
        i = l.get_round_number()
        l.play_round()
        r = l.get_round(i)

        classifications = l.get_actual_puntuations()#r.get_puntuation()
        results = r.get_round_results()

        R = round_results.roundResults(classifications, results)
        button_pressed = R.result_dialog.run()

        
        while gtk.events_pending():
            gtk.main_iteration(False)
        if button_pressed == -4:
            band = True
        #del R
        #time.sleep(3)

        #band = R.end_contest
    
