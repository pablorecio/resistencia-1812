# -*- coding: utf-8 -*-

import pygame

import piece

class Board(object):
    """This class represents a complete board of the game.

    Its responsability is to generate and draw a board with all the pieces
    ubicated on int.
    """
    def __init__(self, state, teamA_piece, teamB_piece, default_piece,
                 piece_size=60, board_size=8, value_max=6, hidden=False):
        """Init method for class Board

        Keywords arguments:
        state -- Matrix that represents the actual state of the board, with
        the values of all its pieces.         
        teamA_piece -- Path to the image that represents the pieces of the team A
        teamB_piece -- Path to the image that represents the pieces of the team B
        default_piece -- Path to the image that represents an empty tile
        piece_size --
        board_size --
        value_max --
        hidden --

        It's important to note that the values of the state matrix are in
        [-2*value_max, 2*value_max]. If value == 0, the tile is empty. If value > 0,
        represents a piece of team A, and if value < 0, represents a piece of team B.
        If abs(value) <= value_max, means that the piece value are hidden for the
        other team.
        """
        assert(len(state) == board_size)
        for i in range(len(state)):
            assert(len(state[i]) == board_size)
            
        self.board_state = state
        self.piece_size = piece_size
        self.board_size = board_size
        self.keys = {}
        self.keys[0] = piece.Piece(0,0,60,img_path=default_piece).get_surface().convert()
        self.value_max = value_max
        self.hidden = hidden

        images = {}
        images[1] = teamA_piece
        images[-1] = teamB_piece

        # next loop will generate the surfaces of every different piece and store
        # them on a dictionary. This way we can make an easy conversion from the
        # piece value to its proper surface.
        for i in range(board_size):
            for j in range(board_size):
                if (self.keys.has_key(state[i][j]) == False):
                    value = abs(state[i][j])
                    team = state[i][j] / value
                    covered = 0
                    if value > value_max:
                        value = value - value_max
                        covered = 1
                    self.keys[state[i][j]] = piece.Piece(value,
                                                         covered,
                                                         60,
                                                         self.hidden,
                                                         images[team]).get_surface().convert()

    def get_surface(self):
        """
        Generate a pygame drawdable surface with the entire board.
        """
        size = (self.board_size*self.piece_size,)*2
        surface = pygame.surface.Surface(size).convert()
        aux_board = _reverse_board(self.board_state)
        for i in range(self.board_size):
            for j in range(self.board_size):
                point = (j*self.piece_size, i*self.piece_size)
                surface.blit(self.keys[aux_board[i][j]],point)

        return surface

def _reverse_board(board):
    tmp_board = []
    n = len(board)
    
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(0)
        tmp_board.append(aux)

    for i in range(n):
        for j in range(n):
            tmp_board[n-(i+1)][j] = board[i][j]

    return tmp_board
