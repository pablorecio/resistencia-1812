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
Provides a class used to represent a board of the game. This board is an
instance or turn of the entire game
"""

import pygame

import guadaboard.piece as piece


class Board(object):
    """This class represents a complete board of the game.

    Its responsability is to generate and draw a board with all the pieces
    ubicated on int.
    """
    def __init__(self, state, team_a_piece, team_b_piece, default_piece,
                 piece_size=60, board_size=8, value_max=6, hidden=False,
                 identifiers=None, player=None):
        """Init method for class Board

        Keywords arguments:
        state -- Matrix that represents the actual state of the board, with
        the values of all its pieces.
        team_a_piece -- Path to the image that represents the pieces of the
        team A
        team_b_piece -- Path to the image that represents the pieces of
        the team
        default_piece -- Path to the image that represents an empty tile
        piece_size --
        board_size --
        value_max --
        hidden --

        It's important to note that the values of the state matrix are in
        [-2*value_max, 2*value_max]. If value == 0, the tile is empty.
        If value > 0, represents a piece of team A, and if value < 0,
        represents a piece of team B. If abs(value) <= value_max, means
        that the piece value are hidden for the other team.
        """
        assert(len(state) == board_size)
        for i in range(len(state)):
            assert(len(state[i]) == board_size)

        self.board_state = _reverse_board(state)
        self.piece_size = piece_size
        self.board_size = board_size
        self.keys = {}
        self.pieces_rects = []
        _piece = piece.Piece(0, 0, 60, img_path=default_piece)
        self.keys[0] = _piece.get_surface().convert()
        self.value_max = value_max
        self.hidden = hidden
        if not identifiers == None:
            self.identifiers = _reverse_board(identifiers)

        images = {}
        images[1] = team_a_piece
        images[-1] = team_b_piece
        #if player == 'A':
        #    self.player_team = 1
        #else:
        print player
        self.player_team = player

        # next loop will generate the surfaces of every different piece and
        # store them on a dictionary. This way we can make an easy conversion
        # from the piece value to its proper surface.
        for i in range(board_size):
            for j in range(board_size):
                if not state[i][j] in self.keys:
                    value = abs(state[i][j])
                    team = state[i][j] / value
                    covered = 0
                    rhidde = self.hidden
                    if not (identifiers == None) and rhidde == True:
                        if team == self.player_team:
                            rhidde = False
                    if value > value_max:
                        value = value - value_max
                        covered = 1
                    _piece = piece.Piece(
                        value, covered, 60, rhidde, images[team])
                    self.keys[state[i][j]] = _piece.get_surface().convert()
        print 'termina board.Board()'

    def get_surface(self):
        """
        Generate a pygame drawdable surface with the entire board.
        """
        print 'get_surface'
        size = (self.board_size * self.piece_size, ) * 2
        surface = pygame.surface.Surface(size).convert()
        #aux_board = _reverse_board(self.board_state)
        aux_board = self.board_state
        self.pieces_rects = []
        for i in range(self.board_size):
            aux = []
            for j in range(self.board_size):
                point = (j * self.piece_size, i * self.piece_size)
                aux.append(surface.blit(self.keys[aux_board[i][j]], point))
            self.pieces_rects.append(aux)

        return surface

    def check_collision(self, pos, offset=(0, 0)):
        """
        Check if a point collides with a piece
        """
        real_pos = (pos[0] - offset[0], pos[1] - offset[1])
        print pos
        print real_pos
        print offset

        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.pieces_rects[i][j].collidepoint(real_pos):
                    print 'seleccionado'
                    team = 0
                    if not self.board_state[i][j] == 0:
                        _abs_state = abs(self.board_state[i][j])
                        team = self.board_state[i][j] / _abs_state
                    print (self.identifiers[i][j], (i, j), team)
                    return (self.identifiers[i][j], (i, j), team)


def _reverse_board(board):
    """
    On the kernel, with the origin swapped. So we have to reverse the board.
    Returns the same board but reversed
    """
    tmp_board = []
    _number = len(board)

    for i in range(_number):
        aux = []
        for j in range(_number):
            aux.append(0)
        tmp_board.append(aux)

    for i in range(_number):
        for j in range(_number):
            tmp_board[_number - (i + 1)][j] = board[i][j]

    return tmp_board
