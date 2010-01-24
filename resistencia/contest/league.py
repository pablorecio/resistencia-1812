# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# This file is part of Resistencia Cadiz 1812.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Copyright (C) 2010, Pablo Recio Quijano
#----------------------------------------------------------------------

import sys
import time

import os
import datetime
import random

from resistencia import configure
import pairing
import round

def _extract_name(team):
    i = team[0].find("/reglas")
    j = team[0].find(".clp")

    return (team[0])[i+7:j]

def _generate_tournament_file_name():
    t = datetime.datetime.now()

    if (t.month < 10):
        month = "0" + str(t.month)
    else:
        month = str(t.month)
            
    if (t.day < 10):
        day = "0" + str(t.day)
    else:
        day = str(t.day)

    if (t.hour < 10):
        hour = "0" + str(t.hour)
    else:
        hour = str(t.hour)
    
    if (t.minute < 10):
        min = "0" + str(t.minute)
    else:
        min = str(t.minute)
    
    des = 'tournament_' + str(t.year) + "-" + month + "-"
    des += day + "_" + hour + ":" + min
    des += ".txt"
    
    base_path = configure.load_configuration()['games_path']
    
    return base_path + '/' + des

def _generate_key_names(teams):
    d = {}

    for team in teams:
        name = _extract_name(team)
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
        self.tournament_file_name = _generate_tournament_file_name()
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

    teams = [('../teams/reglasRafa.clp', '../teams/equipoRafa.clp'),
             ('../teams/reglasJavierS.clp', '../teams/equipoJavierS.clp'),
             ('../teams/reglasPabloRecio.clp','../teams/equipoPabloRecio.clp'),
             ('../teams/reglasRosunix.clp', '../teams/equipoRosunix.clp'),
             ('../teams/reglasGent0oza.clp', '../teams/equipoGent0oza.clp'),
             ('../teams/reglasAbrahan.clp', '../teams/equipoAbrahan.clp'),
             ('../teams/reglasPalomo.clp', '../teams/equipoPalomo.clp'),
             ('../teams/reglasNoelia.clp', '../teams/equipoNoelia.clp')]

    l = League(teams, True)

    while not l.league_completed:
        l.play_round()
        l.print_actual_puntuations()

        time.sleep(10)
    
