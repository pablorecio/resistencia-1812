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

# Copyright (C) 2009, Pablo Recio Quijano
#----------------------------------------------------------------------

import os
import sys
from xml.dom import minidom

import pygame
import pygame.font

import main_layout_functions as functions

# To clarify this, here is a little schema of the list 'self.elements'
# after reading the XML file:
#
# - 'title'
# - 'background'
# - 'favicon'
# - 'font_type'
# - 'font_syze'
# - 'font_color'
# - 'window_size'
# - 'board'
#   |- 'board_size'
#   |- 'board_position'
# - 'players_names'
#   |- 'names_background'
#   |- 'names_size'
#   |- 'names_position'
#   |- 'inside_Labels'
#      |- 'piece_position'
#      |- 'piece_size'
#      |- 'name_position'
#      |- 'label_A_position'
#      |- 'label_B_position'
# - 'action_buttons'
#   |- 'action_buttons_size'
#   |- 'action_buttons_postion'
#   |- 'first_button'
#      |- 'first_button_size'
#      |- 'first_button_position'
#      |- 'first_button_images'
#   |- 'second_button'
#      |- 'second_button_size'
#      |- 'second_button_position'
#      |- 'second_button_images'
#   |- 'third_button'
#      |- 'third_button_size'
#      |- 'third_button_position'
#      |- 'third_button_images'
#   |- 'fourth_button'
#      |- 'fourth_button_size'
#      |- 'fourth_button_position'
#      |- 'fourth_button_images'
# - 'exit_button'
#   |- 'exit_button_size'
#   |- 'exit_button_position'
#   |- 'exit_button_images'

class Layout(object):
    def __init__(self, xml_layout_document, interaction=False):
        self._color_key = (255,0,255)
        self.elements = {}
        self.interaction = interaction
        docxml = minidom.parse(xml_layout_document)

        window_board = docxml.firstChild
        window_board_childs = window_board.childNodes

        functions.erase_childs_end_of_line(window_board_childs)

        for element in window_board_childs:
            tag = element.tagName
            attr = element.getAttribute('type')
            
            x = eval('functions.parse_' + tag + '_' + attr + '(element)')
            self.elements[element.getAttribute('name')] = x
        
        self.window_size = self.elements['window_size']
        self.window_title = self.elements['window_title']
        self.state = {'button_exit': 0, 'button_left_2': 0, 'button_left_1': 0,
                      'button_right_1': 0, 'button_right_2': 0}

    def init(self, player_A, player_B, initial_board):
        self.favicon = pygame.image.load(self.elements['favicon'])

        self.player_A = player_A
        self.player_B = player_B

        self.board = initial_board

        self._create_labels()
        self._create_buttons()

        self._buttons_rects = self._generate_buttons_rects()

        self._static_background = self._get_static_surface()
        self._buttons_rects
        

    def _create_labels(self): #redimensionar las fichas
        piece_size = self.elements['players_names']['inside_labels']['piece_size']
        label_A = pygame.image.load(self.elements['players_names']['names_background']).convert()
        label_B = pygame.image.load(self.elements['players_names']['names_background']).convert()

        piece_A = pygame.transform.scale(pygame.image.load(self.player_A[0]), piece_size)
        piece_B = pygame.transform.scale(pygame.image.load(self.player_B[0]), piece_size)

        name_font = pygame.font.Font(self.elements['font_type'], 22)

        name_A = name_font.render(self.player_A[1], 1, self.elements['font_color'])
        name_B = name_font.render(self.player_B[1], 1, self.elements['font_color'])

        piece_position = self.elements['players_names']['inside_labels']['piece_position']
        text_position = self.elements['players_names']['inside_labels']['name_position']
        label_A.blit(piece_A, piece_position)
        label_A.blit(name_A, text_position)
        
        label_B.blit(piece_B, piece_position)
        label_B.blit(name_B, text_position)

        self.labels = (label_A, label_B)

    def _create_buttons(self):
        button_exit_path = self.elements['exit_button']['exit_button_images']
        button_left_2_path = self.elements['action_buttons']['first_button']['first_button_images']
        button_left_1_path = self.elements['action_buttons']['second_button']['second_button_images']
        button_right_1_path = self.elements['action_buttons']['third_button']['third_button_images']
        button_right_2_path = self.elements['action_buttons']['fourth_button']['fourth_button_images']
        self.buttons = {}

        button_exit_default = pygame.image.load(button_exit_path[0])
        button_exit_above = pygame.image.load(button_exit_path[1])
        button_exit_pressed = pygame.image.load(button_exit_path[2])
        self.buttons['button_exit'] = (button_exit_default, button_exit_above, button_exit_pressed)
        
        button_left_2_default = pygame.image.load(button_left_2_path[0])
        button_left_2_above = pygame.image.load(button_left_2_path[1])
        button_left_2_pressed = pygame.image.load(button_left_2_path[2])
        self.buttons['button_left_2'] = (button_left_2_default, button_left_2_above, button_left_2_pressed)
        
        button_left_1_default = pygame.image.load(button_left_1_path[0])
        button_left_1_above = pygame.image.load(button_left_1_path[1])
        button_left_1_pressed = pygame.image.load(button_left_1_path[2])
        self.buttons['button_left_1'] = (button_left_1_default, button_left_1_above, button_left_1_pressed)
        
        button_right_1_default = pygame.image.load(button_right_1_path[0])
        button_right_1_above = pygame.image.load(button_right_1_path[1])
        button_right_1_pressed = pygame.image.load(button_right_1_path[2])
        self.buttons['button_right_1'] = (button_right_1_default, button_right_1_above, button_right_1_pressed)
        
        button_right_2_default = pygame.image.load(button_right_2_path[0])
        button_right_2_above = pygame.image.load(button_right_2_path[1])
        button_right_2_pressed = pygame.image.load(button_right_2_path[2])
        self.buttons['button_right_2'] = (button_right_2_default, button_right_2_above, button_right_2_pressed)
        
    def _draw_background(self):
        return pygame.image.load(self.elements['background']).convert()
    
    def _draw_labels(self):
        labels_size = self.elements['players_names']['names_size']
        label_A_pos = self.elements['players_names']['inside_labels']['label_A_position']
        label_B_pos = self.elements['players_names']['inside_labels']['label_B_position']
        
        labels = pygame.Surface(labels_size)
        labels.set_colorkey(self._color_key)
        labels.fill(self._color_key)
        
        labels.blit(self.labels[0], label_A_pos)
        labels.blit(self.labels[1], label_B_pos)

        return labels
    
    def _draw_exit_button(self):
        return self.buttons['button_exit'][self.state['button_exit']]

    def _draw_buttons(self):
        buttons_size = self.elements['action_buttons']['action_buttons_size']
        button_1 = self.buttons['button_left_2'][self.state['button_left_2']]
        button_2 = self.buttons['button_left_1'][self.state['button_left_1']]
        button_3 = self.buttons['button_right_1'][self.state['button_right_1']]
        button_4 = self.buttons['button_right_2'][self.state['button_right_2']]
        
        buttons = []
        
        buttons.append((button_1, self.elements['action_buttons']['first_button']['first_button_position']))
        buttons.append((button_2, self.elements['action_buttons']['second_button']['second_button_position']))
        buttons.append((button_3, self.elements['action_buttons']['third_button']['third_button_position']))
        buttons.append((button_4, self.elements['action_buttons']['fourth_button']['fourth_button_position']))
        
        buttons_srfc = pygame.Surface(buttons_size)
        buttons_srfc.set_colorkey(self._color_key)
        buttons_srfc.fill(self._color_key)
        
        for button in buttons:
            buttons_srfc.blit(button[0],button[1])
            
        return buttons_srfc
        
    def change_board(self, board):
        self.board = board

    def get_board_position(self):
        return self.elements['board']['board_position']

    def get_favicon(self):
        return self.favicon

    def get_window_size(self):
        return self.window_size

    def get_window_title(self):
        return self.window_title

    def _get_absolute_position(self, pos1, pos2):
        return (pos1[0] + pos2[0], pos1[1] + pos2[1])

    def _generate_buttons_rects(self):
        surface = pygame.Surface(self.window_size)

        button_exit = self.buttons['button_exit'][0]
        if not self.interaction:
            button_1 = self.buttons['button_left_2'][0]
            button_2 = self.buttons['button_left_1'][0]
            button_3 = self.buttons['button_right_1'][0]
            button_4 = self.buttons['button_right_2'][0]

        exit_button_pos = self.elements['exit_button']['exit_button_position']

        if not self.interaction:
            action_buttons_pos = self.elements['action_buttons']['action_buttons_position']
            
            left_2_button_pos = self.elements['action_buttons']['first_button']['first_button_position']
            left_2_button_pos = self._get_absolute_position(action_buttons_pos,
                                                            left_2_button_pos)

            left_1_button_pos = self.elements['action_buttons']['second_button']['second_button_position']
            left_1_button_pos = self._get_absolute_position(action_buttons_pos,
                                                            left_1_button_pos)

            right_1_button_pos = self.elements['action_buttons']['third_button']['third_button_position']
            right_1_button_pos = self._get_absolute_position(action_buttons_pos,
                                                             right_1_button_pos)

            right_2_button_pos = self.elements['action_buttons']['fourth_button']['fourth_button_position']
            right_2_button_pos = self._get_absolute_position(action_buttons_pos,
                                                             right_2_button_pos)

        rects = {}
        rects['button_exit'] = surface.blit(button_exit, exit_button_pos)
        if not self.interaction:
            rects['button_left_2'] = surface.blit(button_1, left_2_button_pos)
            rects['button_left_1'] = surface.blit(button_2, left_1_button_pos)
            rects['button_right_1'] = surface.blit(button_3, right_1_button_pos)
            rects['button_right_2'] = surface.blit(button_4, right_2_button_pos)

        return rects

    def get_buttons_rects(self):
        return self._buttons_rects
        
    def _get_static_surface(self):
        label_position = self.elements['players_names']['names_position']
        
        back_surface = pygame.Surface(self.elements['window_size'])
        
        background = self._draw_background()
        labels = self._draw_labels()
        
        back_surface.blit(background,(0,0))
        back_surface.blit(labels, label_position)

        return back_surface

    def get_surface(self, mouse = None):
        exit_position = self.elements['exit_button']['exit_button_position']
        buttons_position = self.elements['action_buttons']['action_buttons_position']
        board_position = self.elements['board']['board_position']

        final_surface = pygame.Surface(self.elements['window_size'])

        if mouse:
            self.state[mouse[0]] = mouse[1]
        else:
            for index in self.state:
                self.state[index] = 0
        exit_button = self._draw_exit_button()
        if not self.interaction:
            buttons = self._draw_buttons()

        final_surface.blit(self._static_background,(0,0))
        final_surface.blit(self.board, board_position)
        final_surface.blit(exit_button, exit_position)
        if not self.interaction:
            final_surface.blit(buttons, buttons_position)

        return final_surface
