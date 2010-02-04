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

from guadaboard import guada_board
#from resistencia import xdg

import round

class TestRound(round.Round):
    def __init__ (self, matchs, translator, log_file, num_turns = 150, player = 0):
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
            return self.rounds_stats
        else:
            raise round.RoundError('Not all games played')

    def _merge_stats(self, match_stats):
        for k in self.round_stats:
            self.round_stats[k] = self.round_stats[k] + match_stats[k]

    def play_match(self):
        teamA_key = self.round[self.next_game][0][0]
        teamB_key = self.round[self.next_game][0][1]

        teamA = (self.translator[teamA_key],)
        teamB = (self.translator[teamB_key],)

        result, stats = guada_board.run(teamA, teamB, fast=True, get_stats=True,
                                        number_turns = self.number_turns)
        
        self.round[self.next_game] = (self.round[self.next_game][0], True, result)

        self.next_game = self.next_game + 1
        self.completed = (self.next_game == self.number_games)

        self._merge_stats(stats[self.player])

        return (self.round[self.next_game-1][0], self.round[self.next_game-1][2])
        
    
