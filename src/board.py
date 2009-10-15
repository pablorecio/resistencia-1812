# -*- coding: utf-8 -*-

import pygame
import piece

class Board(object):
    """
    """
    def __init__(self, state, teamA_piece, teamB_piece, default_piece,
                 piece_size = 60, board_size = 8):
        """
        """
        assert(len(state) == board_size)
        for i in range(len(state)):
            assert(len(state[i]) == board_size)
            
        self.board_state = state
        self.piece_size = piece_size
        self.board_size = board_size
        self.keys = {}
        self.keys[0] = piece.Piece(0,0,60,default_piece).get_surface().convert()

        images = {}
        images[1] = teamA_piece
        images[-1] = teamB_piece

        for i in range(board_size):
            for j in range(board_size):
                if (self.keys.has_key(state[i][j]) == False):
                    value = abs(state[i][j])
                    team = state[i][j] / value
                    self.keys[state[i][j]] = piece.Piece(value,team,60,images[team]).get_surface().convert()

    def get_surface(self):
        size = (self.board_size*self.piece_size,)*2
        surface = pygame.surface.Surface(size).convert()
        for i in range(self.board_size):
            for j in range(self.board_size):
                point = (j*self.piece_size, i*self.piece_size)
                surface.blit(self.keys[self.board_state[i][j]],point)

        return surface
