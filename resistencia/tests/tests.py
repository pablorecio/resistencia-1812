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
"""
Contains the main function to the execution of tests suites
"""

import csv

import gtk

from resistencia import configure, filenames
from resistencia.contest import pairing

from resistencia.nls import gettext as _

import resistencia.tests.test_round as test_round

def _generate_key_names(teams):
    """
    Extract and generate the key names of the teams
    """
    _dic = {}

    for team in teams:
        name = filenames.extract_name_expert_system(team)
        _dic[name] = team

    return _dic

class TestSuite:
    """
    Class that encapsulates the elements of a test suite
    """
    def __init__(self, main_team, teams, rounds_number, num_turns):
        self.main_team = main_team
        self.teams = teams
        self.num_turns = num_turns
        
        self.translator_teams = _generate_key_names(teams)
        self.translator_main_team = _generate_key_names([main_team])

        self.keys_teams = []
        self.key_main_team = []

        self.rounds_number = rounds_number

        base_path = configure.load_configuration()['games_path'] + '/'
        self.filename = base_path + filenames.generate_filename('stats',
                                                                main_team)

        for _team in self.translator_teams:
            self.keys_teams.append(_team)

        for _team in self.translator_main_team:
            self.key_main_team.append(_team)

        self.translator = self.translator_teams.copy()
        for k in self.translator_main_team:
            self.translator[k] = self.translator_main_team[k]

        self.rounds = []
        stats_writer = csv.writer(open(self.filename, 'w'), delimiter=',',
                                  quotechar='|', quoting=csv.QUOTE_MINIMAL)
        stats_writer.writerow([_('Opponent'), _('As team'),
                               _('Result'), _("Number of turns"),
                               _('Number of pieces'), _("Value of the pieces"),
                               _('Turn when max value piece died')])
        for i in range(self.rounds_number):
            round_games = pairing.test_pairing(self.key_main_team[0],
                                               self.keys_teams, i%2)
            self.rounds.append(test_round.TestRound((round_games,
                                                    self.translator),
                                                    num_turns = self.num_turns,
                                                    log_file=self.filename,
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
        """
        Merge the round stats with the main stats
        """
        for k in self.total_stats:
            self.total_stats[k] = self.total_stats[k] + round_stats[k]

    def run_test_suite(self, progress_bar):
        """
        Executes a test suite
        """
        for i in range(self.rounds_number):
            _round = self.rounds[i]
            _ng = _round.get_number_of_games()

            for j in range(_ng):
                _round.play_match()
                progress_bar.pulse()
                while gtk.events_pending():
                    gtk.main_iteration(False)
            
            self._merge_stats(_round.get_round_stats())

    def get_test_stats(self):
        """
        Return the stats of the test suite
        """
        return self.total_stats
