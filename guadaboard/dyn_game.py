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

import time

import pygame

from resistencia import configure, xdg
from resistencia.nls import gettext as _

import board
import layout

def _find_element_matrix(board, e):
    """
    Check the existence of the element on a matrix.
    """
    sum = 0
    for l in board:
        sum += l.count(e)

    return not sum == 0

class DynGame:
    def __init__(self, teamA, teamB, default_piece, xml_file,
                 piece_size=60, board_size=8, player=0):
        self.turn = 0

        self.teamA_piece = teamA[1]
        self.teamB_piece = teamB[1]
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
        
        self.xml_layout.init((teamA[1], teamA[0]), (teamB[1], teamB[0]),
                             self.srfc_board)
        self.rects = self.xml_layout.get_buttons_rects()
        self.offset = self.xml_layout.get_board_position()
        pygame.display.set_icon(self.xml_layout.get_favicon())
        
        self.screen.blit(self.xml_layout.get_surface(),(0,0))
        pygame.display.flip()

        if self.music:
            music_path = xdg.get_data_path('music/walking_on_old_stones.ogg')
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play()
        
        img_piece_selected_path = xdg.get_data_path('images/piece-selection.png')
        img_possible_move_path = xdg.get_data_path('images/posible-move.png')
        print img_piece_selected_path
        self.piece_selected = pygame.image.load(img_piece_selected_path)
        self.possible_move = pygame.image.load(img_possible_move_path)

    def get_number_of_turns(self):
        return self.turn
    
    def _update_layout(self, board):
        self.xml_layout.change_board(self.srfc_board)
        self.screen.blit(self.xml_layout.get_surface(),(0,0))
        pygame.display.flip()

    def draw_layers(self, state, collision, offset=(0,0)):
        pos = (collision[1][1] * self.piece_size,
               collision[1][0] * self.piece_size)

        new_state = _reverse_board(state)
        orig_pos = collision[1]
        adjacents = [(orig_pos[0] + 1, orig_pos[1]), (orig_pos[0] - 1, orig_pos[1]),
                     (orig_pos[0], orig_pos[1] + 1), (orig_pos[0], orig_pos[1] - 1)]
        avaiable = [True, True, True, True]
        value = new_state[orig_pos[0]][orig_pos[1]]
        team = value / abs(value)

        for i in range(4):
            tmp_pos = adjacents[i]
            max = self.board_size - 1
            if tmp_pos[0] < 0 or tmp_pos[1] < 0 or tmp_pos[0] > max or tmp_pos[1] > max:
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
            
        self._update_layout(self.srfc_board)

    def finish(self):
        if self.music:
            pygame.mixer.music.stop()
            pygame.display.quit()

    def draw_boards(self, board_list):
        print 'draw_boards'
        print board_list[0]
        b = None

        for i in board_list:
            state = i[0]
            identifiers = i[1]
            self.turn += 1
            b = board.Board(state, self.teamA_piece, self.teamB_piece,
                            self.default_piece, self.piece_size, self.board_size,
                            identifiers=identifiers, player=self.player, hidden=True)
            print 'vuelta a draw_boards'
            srfc = b.get_surface()

            self.srfc_board.blit(srfc.convert(), (0, 0))
            self._update_layout(self.srfc_board)
            #pygame.display.flip()
            if i != board_list[len(board_list) - 1]:
                time.sleep(2)

        print 'todo pintado'
        band = False
        piece_selected = False
        piece = None
        band_pos = False
        game_continue = _find_element_matrix(state,1) and _find_element_matrix(state,-1)

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
                            surface = self.xml_layout.get_surface((res,2))
                            self.screen.blit(surface,(0,0))
                            pygame.display.flip()                        
                            band_pos = True
                    else:
                        if band_pos == True:
                            surface = self.xml_layout.get_surface()
                            self.screen.blit(surface,(0,0))
                            pygame.display.flip()
                            band_pos = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if _get_collision(event.pos, self.rects) == 'button_exit':
                            if self.music:
                                pygame.mixer.music.stop()
                            pygame.display.quit() 
                        collision = b.check_collision(event.pos)
                        if not piece_selected:
                            if collision[2] == self.player:
                                self.srfc_board.blit(srfc.convert(), (0, 0))
                                self._update_layout(self.srfc_board)
                                #pygame.display.flip()
                                self.draw_layers(state, collision)
                                piece = collision
                                piece_selected = True
                        else: #piece_selected
                            if collision[2] == piece[2]:
                                piece = collision
                                self.srfc_board.blit(srfc.convert(), (0, 0))
                                self._update_layout(self.srfc_board)
                                #pygame.display.flip()
                                self.draw_layers(state, collision)                    
                            elif check_valid_movement(collision, piece):
                                mov = get_movement(piece[1], collision[1], self.player)
                                return (piece[0], mov)
                            #else:
                            #    piece = None
                            #    piece_selected = False


def check_valid_movement(source, dest):
    print source
    print dest
    if source[2] == dest[2]: #same team. maybe handle for a better way
        return false
    else:
        offset_x = abs(source[1][0] - dest[1][0])
        offset_y = abs(source[1][1] - dest[1][1])

        return (offset_x == 1 and offset_y == 0) or (offset_x == 0 and offset_y == 1)

def get_movement(source, dest, team):
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
    res = ''
    for index in rects:
        rect = rects[index]
        if rect.collidepoint(point):
            res = index
            break

    return res

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
