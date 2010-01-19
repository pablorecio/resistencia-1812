# -*- coding: utf-8 -*-

import pygame
import board

class Game(object):
    def __init__(self, entire_game, teamA_piece, teamB_piece,
                 default_piece, piece_size=60, board_size=8, hidden=False):
        self.entire_game = entire_game
        self.turn = 0
        self.num_turn = len(self.entire_game)

        self.teamA_piece = teamA_piece
        self.teamB_piece = teamB_piece
        self.default_piece = default_piece
        self.piece_size = piece_size
        self.board_size = board_size
        self.hidden = hidden

        self.state =  board.Board(self.entire_game[self.turn],
                                  self.teamA_piece, self.teamB_piece, 
                                  self.default_piece, self.piece_size,
                                  self.board_size, hidden=self.hidden)

    def draw_board(self):
        return self.state.get_surface()

    def next_turn(self):
        if self.turn != self.num_turn - 1:
            self.turn = self.turn + 1

            self.state =  board.Board(self.entire_game[self.turn],
                                      self.teamA_piece, self.teamB_piece, 
                                      self.default_piece, self.piece_size,
                                      self.board_size, hidden=self.hidden)

    def previous_turn(self):
        if self.turn != 0:
            self.turn = self.turn - 1

            self.state =  board.Board(self.entire_game[self.turn],
                                      self.teamA_piece, self.teamB_piece, 
                                      self.default_piece, self.piece_size,
                                      self.board_size, hidden=self.hidden)

    def first_turn(self):
        self.turn = 0

        self.state =  board.Board(self.entire_game[self.turn],
                                  self.teamA_piece, self.teamB_piece, 
                                  self.default_piece, self.piece_size,
                                  self.board_size, hidden=self.hidden)

    def last_turn(self):
        self.turn = self.num_turn - 1

        self.state =  board.Board(self.entire_game[self.turn],
                                  self.teamA_piece, self.teamB_piece, 
                                  self.default_piece, self.piece_size,
                                  self.board_size, hidden=self.hidden)
