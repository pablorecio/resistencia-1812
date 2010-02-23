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
This module contains the handling of a game for the one player mode.
"""

import time

import pygame

from resistencia import configure, xdg

import guadaboard.board as board
import guadaboard.layout as layout

def _find_element_matrix(board_rep, element):
    """
    Check the existence of the element on a matrix.
    """
    _sum = 0
    for line in board_rep:
        _sum += line.count(element)

    return not _sum == 0

class DynGame:
    """
    This class models a dynamic game. A dynamic game is a way
    to play with one team is an expert system and the other is
    a human.
    """
    def __init__(self, team_a, team_b, default_piece, xml_file,
                 piece_size=60, board_size=8, player=0):
        self.turn = 0

        self.team_a_piece = team_a[1]
        self.team_b_piece = team_b[1]
        self.default_piece = default_piece
        self.piece_size = piece_size
        self.board_size = board_size

        self.srfc_board_size = (self.board_size*self.piece_size,)*2
        self.player = player
        
        self.music = False
        if configure.load_configuration()['music_active'] == '1':
            self.music = True
        
        pygame.init()
        self.xml_layout = layout.Layout(xml_file, True)
        #self.screen = pygame.display.set_mode(self.srfc_board_size)
        self.screen = pygame.display.set_mode(self.xml_layout.get_window_size())
        pygame.display.set_caption(self.xml_layout.get_window_title())
        self.srfc_board = pygame.Surface(self.srfc_board_size)
        
        self.xml_layout.init((team_a[1], team_a[0]), (team_b[1], team_b[0]),
                             self.srfc_board)
        self.rects = self.xml_layout.get_buttons_rects()
        self.offset = self.xml_layout.get_board_position()
        pygame.display.set_icon(self.xml_layout.get_favicon())
        
        self.screen.blit(self.xml_layout.get_surface(), (0, 0))
        pygame.display.flip()

        if self.music:
            music_path = xdg.get_data_path('music/walking_on_old_stones.ogg')
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play()
        
        img_piece_slct_path = xdg.get_data_path('images/piece-selection.png')
        img_possible_move_path = xdg.get_data_path('images/posible-move.png')
        print img_piece_slct_path
        self.piece_selected = pygame.image.load(img_piece_slct_path)
        self.possible_move = pygame.image.load(img_possible_move_path)

    def get_number_of_turns(self):
        """
        Returns the number of turns played
        """
        return self.turn
    
    def _update_layout(self):
        """
        Update the layout with a board surface
        """
        self.xml_layout.change_board(self.srfc_board)
        self.screen.blit(self.xml_layout.get_surface(), (0, 0))
        pygame.display.flip()

    def draw_layers(self, state, collision):
        """
        Draw the layers that represents the focused piece and
        the possible movements
        """
        pos = (collision[1][1] * self.piece_size,
               collision[1][0] * self.piece_size)

        new_state = _reverse_board(state)
        orig_pos = collision[1]
        adjacents = [(orig_pos[0] + 1, orig_pos[1]),
                     (orig_pos[0] - 1, orig_pos[1]),
                     (orig_pos[0], orig_pos[1] + 1),
                     (orig_pos[0], orig_pos[1] - 1)]
        avaiable = [True, True, True, True]
        value = new_state[orig_pos[0]][orig_pos[1]]
        team = value / abs(value)

        for i in range(4):
            tmp_pos = adjacents[i]
            max_val = self.board_size - 1
            first_band = tmp_pos[0] < 0 or tmp_pos[1] < 0
            if first_band or tmp_pos[0] > max_val or tmp_pos[1] > max_val:
                avaiable[i] = False
            else:
                val = new_state[tmp_pos[0]][tmp_pos[1]]
                if not val == 0:
                    if val / abs(val) == team:
                        avaiable[i] = False
        self.srfc_board.blit(self.piece_selected, pos)
        for i in range(4):
            if avaiable[i]:
                new_pos = (adjacents[i][1] * self.piece_size,
                           adjacents[i][0] * self.piece_size)
                self.srfc_board.blit(self.possible_move, new_pos)
            
        self._update_layout()

    def finish(self):
        """
        Stop the pygame environment
        """
        if self.music:
            pygame.mixer.music.stop()
            pygame.display.quit()

    def draw_boards(self, board_list):
        """
        Draw a board a capture the movement of the user
        """
        print 'draw_boards'
        print board_list[0]
        _board = None

        for i in board_list:
            state = i[0]
            identifiers = i[1]
            self.turn += 1
            _board = board.Board(state, self.team_a_piece, self.team_b_piece,
                                 self.default_piece, self.piece_size,
                                 self.board_size, identifiers=identifiers,
                                 player=self.player, hidden=True)
            print 'vuelta a draw_boards'
            srfc = _board.get_surface()

            self.srfc_board.blit(srfc.convert(), (0, 0))
            self._update_layout()
            #pygame.display.flip()
            if i != board_list[len(board_list) - 1]:
                time.sleep(2)

        print 'todo pintado'
        band = False
        piece_selected = False
        piece = None
        band_pos = False
        find_element_1 = _find_element_matrix(state, 1)
        find_element_neg_1 = _find_element_matrix(state, -1)
        game_continue = find_element_1 and find_element_neg_1

        clock = pygame.time.Clock()
        while not band and game_continue:
            time_passed = clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if self.music:
                        pygame.mixer.music.stop()
                    pygame.display.quit()
                elif event.type == pygame.MOUSEMOTION:
                    res = _get_collision(event.pos, self.rects)
                    if res != '':
                        if band_pos == False:
                            surface = self.xml_layout.get_surface((res, 2))
                            self.screen.blit(surface, (0, 0))
                            pygame.display.flip()                        
                            band_pos = True
                    else:
                        if band_pos == True:
                            surface = self.xml_layout.get_surface()
                            self.screen.blit(surface, (0, 0))
                            pygame.display.flip()
                            band_pos = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if _get_collision(event.pos,
                                          self.rects) == 'button_exit':
                            if self.music:
                                pygame.mixer.music.stop()
                            pygame.display.quit() 
                        collision = _board.check_collision(event.pos)
                        if not piece_selected:
                            if collision[2] == self.player:
                                self.srfc_board.blit(srfc.convert(), (0, 0))
                                self._update_layout()
                                #pygame.display.flip()
                                self.draw_layers(state, collision)
                                piece = collision
                                piece_selected = True
                        else: #piece_selected
                            if collision[2] == piece[2]:
                                piece = collision
                                self.srfc_board.blit(srfc.convert(), (0, 0))
                                self._update_layout()
                                #pygame.display.flip()
                                self.draw_layers(state, collision)
                            elif check_valid_movement(collision, piece):
                                mov = get_movement(piece[1], collision[1],
                                                   self.player)
                                return (piece[0], mov)
                            #else:
                            #    piece = None
                            #    piece_selected = False


def check_valid_movement(source, dest):
    """
    Checks if a movement is valid or not
    """
    print source
    print dest
    if source[2] == dest[2]: #same team. maybe handle for a better way
        return False
    else:
        offset_x = abs(source[1][0] - dest[1][0])
        offset_y = abs(source[1][1] - dest[1][1])

        element_1 = offset_x == 1 and offset_y == 0
        element_2 = offset_x == 0 and offset_y == 1

        return element_1 or element_2

def get_movement(source, dest, team):
    """
    Get the movement realized for the user
    """
    mov = 0
    if source[1] == dest[1]: #vertical movement
        res = source[0] - dest[0]
        if res == -1: #down
            if team == 1: #team A
                mov = 4
            else: #team B
                mov = 3
        else: #up
            if team == 1: #team A
                mov = 3
            else: #team B
                mov = 4
    else: #horizontal movement
        res = source[1] - dest[1]
        if res == 1: #left
            if team == 1: #team A
                mov = 2
            else: #team B
                mov = 1
        else: #right
            if team == 1: #team A
                mov = 1
            else: #team B
                mov = 2

    return mov


def _get_collision(point, rects):
    """
    Checks the collising of the rects
    """
    res = ''
    for index in rects:
        rect = rects[index]
        if rect.collidepoint(point):
            res = index
            break

    return res

def _reverse_board(_board):
    """
    Reverse the board from the guadalete kernel
    """
    tmp_board = []
    _num = len(_board)
    
    for i in range(_num):
        aux = []
        for j in range(_num):
            aux.append(0)
        tmp_board.append(aux)

    for i in range(_num):
        for j in range(_num):
            tmp_board[_num-(i+1)][j] = _board[i][j]

    return tmp_board
