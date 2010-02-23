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
"""
Contains the class that specializes the round class of the competition, to
be used on the tests.
"""

import csv

from guadaboard import guada_board
#from resistencia import xdg

from resistencia.contest import round as contest_round

class TestRound(contest_round.Round):
    """
    This class includes the same values that a contest round.

    On the __init__ method, teams is a tuple with the fist value a list of
    matchs, and the second has the translator of the keys that contains
    the real team
    """
    def __init__ (self, teams, num_turns = 150,
                  log_file=None, player = 0):
        #player must be 0 or 1
        contest_round.Round.__init__(self, teams[0], teams[1],
                                     log_file, num_turns)
        self.player_team = player

        self.round_stats = {}
        self.round_stats['wins'] = 0
        self.round_stats['looses'] = 0
        self.round_stats['draws'] = 0
        self.round_stats['turns_winning'] = 0
        self.round_stats['turns_losing'] = 0
        self.round_stats['num_pieces'] = 0
        self.round_stats['val_pieces'] = 0
        self.round_stats['max_death'] = 0

    def get_round_stats(self):
        """
        Returns a list with the stats of the tests rounds
        """
        if self.completed:
            return self.round_stats
        else:
            raise contest_round.RoundError('Not all games played')

    def _merge_stats(self, match_stats):
        """
        Merge the stats of a match with the general stats.
        """
        for k in match_stats:
            self.round_stats[k] = self.round_stats[k] + match_stats[k]

    def play_match(self, fast=None, cant_draw=None):
        """
        Run a simulation of the next game on the round
        """
        teams_keys = {}
        teams_keys['a'] = self.round[self.next_game][0][0]
        teams_keys['b'] = self.round[self.next_game][0][1]

        team_a = (self.translator[teams_keys['a']],)
        team_b = (self.translator[teams_keys['b']],)

        result, stats = guada_board.run(team_a, team_b, fast=True,
                                        get_stats=True,
                                        number_turns=self.num_turns,
                                        dont_log=True)

        stats_writer = csv.writer(open(self.log_file, 'a'), delimiter=',')#,
                                  #quotechar='|', quoting=csv.QUOTE_MINIMAL)
        key_result = ''
        player_stats = stats[self.player_team]
        number_of_turns = 0

        key = ''
        team = ''
        if self.player_team == 0:
            key = teams_keys['b']
            team = 'A'
            if result == 1:
                number_of_turns = player_stats['turns_winning']
                key_result = 'A'
            elif result == -1:
                number_of_turns = player_stats['turns_losing']
                key_result = 'B'
            else:
                key_result = 'D'
        else:
            key = teams_keys['a']
            team = 'B'
            if result == -1:
                number_of_turns = player_stats['turns_winning']
                key_result = 'A'
            elif result == 1:
                number_of_turns = player_stats['turns_losing']
                key_result = 'B'
            else:
                key_result = 'D'
        write_results = [key, team, key_result, number_of_turns,
                         player_stats['num_pieces'],
                         player_stats['val_pieces'],
                         player_stats['max_death']]
        print write_results

        stats_writer.writerow(write_results)
                             
        self.round[self.next_game] = (self.round[self.next_game][0],
                                      True, result)

        self.next_game = self.next_game + 1
        self.completed = (self.next_game == self.number_games)

        self._merge_stats(stats[self.player_team])

        return (self.round[self.next_game-1][0],
                self.round[self.next_game-1][2])
        
    
