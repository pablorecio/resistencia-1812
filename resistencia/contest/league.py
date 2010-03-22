# -*- coding: utf-8 -*-
###############################################################################
# This file is part of Resistencia en Cadiz: 1812.                            #
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
import gtk

from resistencia import configure, filenames

import pairing
import contest
import round

class League(contest.Contest):
    
    def __init__(self, teams, num_turns, back_round=False):
        self.teams = teams
        self.translator = contest.generate_key_names(teams)
        self.keys = []
        self.num_turns = num_turns

        for t in self.translator:
            self.keys.append(t)

        self.matchs = pairing.make_pairings(self.keys, back_round)

        self.rounds = []
        base_path = configure.load_configuration()['games_path'] + '/'
        self.tournament_file_name = base_path + filenames.generate_filename('league')
        print self.tournament_file_name
        
        for jorn in self.matchs:
            self.rounds.append(round.Round(jorn, self.translator,
                                           self.tournament_file_name,
                                           self.num_turns))

        self.puntuations_by_round = []
        self.puntuations = {}
        for key in self.keys:
            self.puntuations[key] = 0

        self.number_of_rounds = len(self.rounds)
        self.actual_round = 0
        self.league_completed = False

    def get_round_number(self):
        return self.actual_round
    
    def get_prev_round_number(self):
        return self.actual_round - 1

    def get_number_of_rounds(self):
        return self.number_of_rounds

    def get_round(self, round_number):
        return self.rounds[round_number]

    def play_round(self, progress_bar, fast=False):
        if not self.league_completed:
            r = self.rounds[self.actual_round]
            n = r.get_number_of_games()

            for i in range(n):
                if fast:
                    progress_bar.pulse()
                    while gtk.events_pending():
                        gtk.main_iteration(False)
                r.play_match(fast)

            p = r.get_puntuation()
            self.puntuations_by_round.append(p)
            contest.merge_puntuations(self.puntuations, p)

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
        clasification.sort(contest.puntuations_compare)
        clasification.reverse()

        return clasification

    def print_actual_puntuations(self):
        clasification = self.puntuations.items()
        clasification.sort(contest.puntuations_compare)
        clasification.reverse()

        for i in clasification:
            name = i[0]
            punt = i[1]

            if not name == 'aux_ghost_team':
                long_name = len(name)
                
                num_sep = 29 - long_name

                print name + ' ' + '-'*num_sep + ' ' + str(punt)

    
