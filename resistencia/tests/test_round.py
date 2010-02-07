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

import time
import csv

from guadaboard import guada_board
#from resistencia import xdg

from resistencia.contest import round

class TestRound(round.Round):
    def __init__ (self, matchs, translator, num_turns = 150,
                  log_file=None, player = 0):
        #player must be 0 or 1
        round.Round.__init__(self, matchs, translator, log_file, num_turns)
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
        if self.completed:
            return self.round_stats
        else:
            raise round.RoundError('Not all games played')

    def _merge_stats(self, match_stats):
        for k in match_stats:
            self.round_stats[k] = self.round_stats[k] + match_stats[k]

    def play_match(self):
        teamA_key = self.round[self.next_game][0][0]
        teamB_key = self.round[self.next_game][0][1]

        teamA = (self.translator[teamA_key],)
        teamB = (self.translator[teamB_key],)

        print teamA
        print teamB

        result, stats = guada_board.run(teamA, teamB, fast=True, get_stats=True,
                                        number_turns=self.num_turns, dont_log=True)

        print self.log_file
        stats_writer = csv.writer(open(self.log_file, 'a'), delimiter=',')#,
                                  #quotechar='|', quoting=csv.QUOTE_MINIMAL)
        key_result = ''
        player_stats = stats[self.player_team]
        number_of_turns = 0

        key = ''
        team = ''
        if self.player_team == 0:
            key = teamB_key
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
            key = teamA_key
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
                             
        self.round[self.next_game] = (self.round[self.next_game][0], True, result)

        self.next_game = self.next_game + 1
        self.completed = (self.next_game == self.number_games)

        self._merge_stats(stats[self.player_team])

        return (self.round[self.next_game-1][0], self.round[self.next_game-1][2])
        
    
