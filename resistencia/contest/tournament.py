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

import math
import random

import gtk

from resistencia import configure, filenames

import contest
import round

def _auto_pairings(elements):
    if len(elements) % 2 == 1:
        elements.append('aux_ghost_team')
    random.shuffle(elements)
    
    n = len(elements)

    pairing = []
    for i in range(n/2):
        pairing.append((elements[i],elements[n-i-1]))

    return pairing

def _extract_teams_from_pairing(elements):
    teams = []
    for i in elements:
        teams.append(i[0])
        teams.append(i[1])
    
class Tournament(contest.Contest):
    def __init__(self, teams, num_turns, pairings_done=False):
        self.matchs = []
        self.teams = []
        self.round_winners = []
        self.num_turns = num_turns
        if pairings_done:
            self.matchs.append(teams)
            self.teams = _extract_teams_from_pairing(self.matchs)
        else:
            self.teams = teams

        self.translator = contest.generate_key_names(self.teams)
        self.keys = []
        
        for t in self.translator:
            self.keys.append(t)

        if not pairings_done:
            self.matchs.append(_auto_pairings(self.keys))

        self.round_number = 0
        self.rounds = []
        
        base_path = configure.load_configuration()['games_path'] + '/'
        self.tournament_file_name = base_path + filenames.generate_filename('tournament')
        
        self.rounds.append(round.Round(self.matchs[self.round_number],
                                       self.translator,
                                       self.tournament_file_name,
                                       self.num_turns))

        self.number_of_rounds = int(math.ceil(math.log(len(self.teams),2)))
        self.tournament_completed = False
    
    def get_round_number(self):
        return self.round_number

    def get_prev_round_number(self):
        return self.round_number - 1
    
    def get_number_of_rounds(self):
        return self.number_of_rounds

    def get_round(self, round_number):
        return self.rounds[round_number]

    def play_round(self, progress_bar, fast=False):
        if not self.tournament_completed:
            r = self.rounds[self.round_number]
            n = r.get_number_of_games()
            
            for i in range(n):
                if fast:
                    progress_bar.pulse()
                    while gtk.events_pending():
                        gtk.main_iteration(False)
                r.play_match(fast, True)

            winners = r.get_winners()
            self.round_winners.append(winners)
            
            f_log = open(self.tournament_file_name, 'a')
            f_log.write('Ronda ' + str(self.round_number+1) + ":\n")
            f_log.close()
            r.log_tournament(True)
            f_log = open(self.tournament_file_name, 'a')
            f_log.write('-------------------------------' + "\n")
            f_log.close()
            
            self.round_number = self.round_number + 1
            self.league_completed = (self.round_number == self.number_of_rounds)

            if not self.league_completed:
                self.matchs.append(_auto_pairings(winners))
                self.rounds.append(round.Round(self.matchs[self.round_number],
                                               self.translator,
                                               self.tournament_file_name))

    def get_results_by_now(self):
        return self.round_winners
        
        
        
