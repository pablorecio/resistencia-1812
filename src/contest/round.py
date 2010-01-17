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

import guada_board
pieceA = './images/piece-orange.png'
pieceB = './images/piece-violete.png'

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class RoundError(Error):
    """Exception raised for errors in the round iteration

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.msg = msg

class Round(object):

    def __init__(self, matchs, translator):
        self.round = [] #Formed by tuples ((teamA, teamB), played, result)
        for match in matchs:
            self.round.append((match, False, 0))

        self.completed = False
        self.next_game = 0
        self.number_games = len(self.round)
        self.translator = translator
        
    def get_result(self, id_game):
        if self.round[id_game][1] == True:
            return (self.round[id_game][0], self.round[id_game][2])
        else:
            raise RoundError('The game ' + str(id_game) + ' has not been played yet')

    def get_number_of_games(self):
        return self.number_games

    def get_winners(self):
        winners = []
        if self.completed:
            for match in self.round:
                result = match[2]
                if result == 1:
                    winners.append(match[0][0])
                elif result == -1:
                    winners.append(match[0][1])

            return winners
        else:
            raise RoundError('Not all games played')

    def get_puntuation(self):
        results = {}
        if self.completed:
            for match in self.round:
                result = match[2]
                teamA = match[0][0]
                teamB = match[0][1]
                if result == 0:
                    results[teamA] = 1
                    results[teamB] = 1
                elif result == 1:
                    results[teamA] = 3
                    results[teamB] = 0
                elif result == -1:
                    results[teamA] = 0
                    results[teamB] = 3
            return results
        else:
            raise RoundError('Not all games played')

    def play_match(self):
        teamA_key = self.round[self.next_game][0][0]
        teamB_key = self.round[self.next_game][0][1]
        teamA = (self.translator[teamA_key], pieceA)
        teamB = (self.translator[teamB_key], pieceB)
        
        result = guada_board.run(teamA, teamB, fast=True)

        print "The result of the game '" + teamA_key + "' - '"+ teamB_key + "' was:"
        if result == 0:
            print 'Draw'
        elif result == 1:
            print teamA_key + ' won'
        elif result == -1:
            print teamB_key + ' won'

        self.round[self.next_game] = (self.round[self.next_game][0], True, result)
        
        #self.round[self.next_game][1] = True
        #self.round[self.next_game][2] = result

        self.next_game = self.next_game + 1
        self.completed = (self.next_game == self.number_games)

        return (self.round[self.next_game-1][0], self.round[self.next_game-1][2])

    def is_complete(self):
        return self.completed

        
