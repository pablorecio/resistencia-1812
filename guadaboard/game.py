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
This is a module that provides a class that allows to iterate on a guadalete
game, showing the differents boards.
"""

import guadaboard.board as board

class Game(object):
    """
    This class provides the funcionalities to iterate turns on a game.
    """
    def __init__(self, entire_game, team_a_piece, team_b_piece,
                 default_piece, piece_size=60, board_size=8, hidden=False):
        self.entire_game = entire_game
        self.turn = 0
        self.num_turn = len(self.entire_game)

        self.team_a_piece = team_a_piece
        self.team_b_piece = team_b_piece
        self.default_piece = default_piece
        self.piece_size = piece_size
        self.board_size = board_size
        self.hidden = hidden

        self.state =  board.Board(self.entire_game[self.turn],
                                  self.team_a_piece, self.team_b_piece, 
                                  self.default_piece, self.piece_size,
                                  self.board_size, hidden=self.hidden)

    def draw_board(self):
        """
        Returns a pygame surface with the actual state board
        """
        return self.state.get_surface()

    def next_turn(self):
        """
        Iterates to the next turn
        """
        if self.turn != self.num_turn - 1:
            self.turn = self.turn + 1

            self.state =  board.Board(self.entire_game[self.turn],
                                      self.team_a_piece, self.team_b_piece, 
                                      self.default_piece, self.piece_size,
                                      self.board_size, hidden=self.hidden)

    def previous_turn(self):
        """
        Iterates to the previous turn
        """
        if self.turn != 0:
            self.turn = self.turn - 1

            self.state =  board.Board(self.entire_game[self.turn],
                                      self.team_a_piece, self.team_b_piece, 
                                      self.default_piece, self.piece_size,
                                      self.board_size, hidden=self.hidden)

    def first_turn(self):
        """
        Iterates to the first turn
        """
        self.turn = 0

        self.state =  board.Board(self.entire_game[self.turn],
                                  self.team_a_piece, self.team_b_piece, 
                                  self.default_piece, self.piece_size,
                                  self.board_size, hidden=self.hidden)

    def last_turn(self):
        """
        Iterates to the last turn
        """
        self.turn = self.num_turn - 1

        self.state =  board.Board(self.entire_game[self.turn],
                                  self.team_a_piece, self.team_b_piece, 
                                  self.default_piece, self.piece_size,
                                  self.board_size, hidden=self.hidden)
