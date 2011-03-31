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

import file_parser

def get_game_file_stats(filename):
    game, winner = file_parser.parse_file(filename)
    game = _normalize_game(game)
    num_turns = len(game)
    final_board = game[num_turns -1]
    
    stats_teamA = {}
    stats_teamB = {}
    
    stats_teamA['wins'] = 0
    stats_teamA['looses'] = 0
    stats_teamA['draws'] = 0
    stats_teamA['turns_winning'] = 0
    stats_teamA['turns_losing'] = 0
    stats_teamB['wins'] = 0
    stats_teamB['looses'] = 0
    stats_teamB['draws'] = 0
    stats_teamB['turns_winning'] = 0
    stats_teamB['turns_losing'] = 0
    
    if winner == 1:
        stats_teamA['wins'] = 1
        stats_teamB['looses'] = 1
        stats_teamA['turns_winning'] = num_turns
        stats_teamB['turns_losing'] = num_turns
    elif winner == -1:
        stats_teamA['looses'] = 1
        stats_teamB['wins'] = 1
        stats_teamA['turns_losing'] = num_turns
        stats_teamB['turns_winning'] = num_turns
    else:
        stats_teamA['draws'] = 1
        stats_teamB['draws'] = 1
    
    stats_teamA['num_pieces'], stats_teamB['num_pieces'] = _count_pieces(final_board)
    stats_teamA['val_pieces'], stats_teamB['val_pieces'] = _count_values(final_board)
    
    stats_teamA['max_death'], stats_teamB['max_death'] = _check_death(6, game)
    
    return (stats_teamA, stats_teamB)

def _find_element_matrix(board, e):
    """
    Check the existence of the element on a matrix.
    """
    sum = 0
    for l in board:
        sum += l.count(e)
        
    return not sum == 0

def _check_death(value, entire_game):
    num_turns = len(entire_game)
    valueA = value
    valueB = value - (2 * value)
    
    bandA = True
    bandB = True
    
    turnA = num_turns
    turnB = num_turns
    
    i = 1
    for board in entire_game:
        if bandA:
            if not _find_element_matrix(board, valueA):
                bandA = False
                turnA = i
        if bandB:
            if not _find_element_matrix(board, valueB):
                bandB = False
                turnB = i
        i = i + 1

    return (turnA, turnB)

def _count_pieces(board):
    piecesA = 0
    piecesB = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not board[i][j] == 0:
                if board[i][j] > 0:
                    piecesA = piecesA + 1
                else:
                    piecesB = piecesB +1
                        
    return (piecesA, piecesB)
    
def _count_values(board):
    valuesA = 0
    valuesB = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not board[i][j] == 0:
                if board[i][j] > 0:
                    valuesA = valuesA + board[i][j]
                else:
                    valuesB = valuesB + abs(board[i][j])
                        
    return (valuesA, valuesB)

def _normalize_game(entire_game):
    games = []
    for board in entire_game:
        new_board = []
        for i in range(len(board)):
            row = []
            for j in range (len(board[i])):
                val = board[i][j]
                if not (val >= -6 and val <= 6):
                    if val > 6:
                        val = val - 6
                    if val < -6:
                        val = val + 6
                row.append(val)
            new_board.append(row)
        games.append(new_board)

    return games
