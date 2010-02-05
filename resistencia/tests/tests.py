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
import gtk

from resistencia import configure, filenames
from resistencia.contest import pairing

import test_round

def _generate_key_names(teams):
    d = {}

    for team in teams:
        name = filenames.extract_name_expert_system(team)
        d[name] = team

    return d

class TestSuite:
    def __init__(self, main_team, teams, rounds_number):
        self.main_team = main_team
        self.teams = teams
        
        self.translator_teams = _generate_key_names(teams)
        self.translator_main_team = _generate_key_names([main_team])

        self.keys_teams = []
        self.key_main_team = []

        self.rounds_number = rounds_number

        for t in self.translator_teams:
            self.keys_teams.append(t)

        for t in self.translator_main_team:
            self.key_main_team.append(t)

        self.translator = self.translator_teams.copy()
        for k in self.translator_main_team:
            self.translator[k] = self.translator_main_team[k]

        self.rounds = []
        for i in range(self.rounds_number):
            round_games = pairing.test_pairing(self.key_main_team[0],
                                               self.keys_teams, i%2)
            self.rounds.append(test_round.TestRound(round_games, self.translator,
                                                    player=i%2))

        self.total_stats = {}
        self.total_stats['wins'] = 0
        self.total_stats['looses'] = 0
        self.total_stats['draws'] = 0
        self.total_stats['turns_winning'] = 0
        self.total_stats['turns_losing'] = 0
        self.total_stats['num_pieces'] = 0
        self.total_stats['val_pieces'] = 0
        self.total_stats['max_death'] = 0

    
    def _merge_stats(self, round_stats):
        for k in self.total_stats:
            self.total_stats[k] = self.total_stats[k] + round_stats[k]

    def run_test_suite(self):
        for i in range(self.rounds_number):
            r = self.rounds[i]
            n = r.get_number_of_games()

            for j in range(n):
                r.play_match()

            self._merge_stats(r.get_round_stats())

    def get_test_stats(self):
        return self.total_stats
