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

"""
To clarify this, here is a little schema of the list 'self.elements'
after reading the XML file:

- 'title'
- 'background'
- 'favicon'
- 'font_type'
- 'font_syze'
- 'font_color'
- 'window_size'
- 'board'
  |- 'board_size'
  |- 'board_position'
- 'players_names'
  |- 'names_background'
  |- 'names_size'
  |- 'names_position'
  |- 'inside_Labels'
     |- 'piece_position'
     |- 'piece_size'
     |- 'name_position'
     |- 'label_A_position'
     |- 'label_B_position'
- 'action_buttons'
  |- 'action_buttons_size'
  |- 'action_buttons_postion'
  |- 'first_button'
     |- 'first_button_size'
     |- 'first_button_position'
     |- 'first_button_images'
  |- 'second_button'
     |- 'second_button_size'
     |- 'second_button_position'
     |- 'second_button_images'
  |- 'third_button'
     |- 'third_button_size'
     |- 'third_button_position'
     |- 'third_button_images'
  |- 'fourth_button'
     |- 'fourth_button_size'
     |- 'fourth_button_position'
     |- 'fourth_button_images'
- 'exit_button'
  |- 'exit_button_size'
  |- 'exit_button_position'
  |- 'exit_button_images'
"""

from xml.dom import minidom

import pygame
import pygame.font

from guadaboard import main_layout_functions as functions

class Layout(object):
    """
    Class that reads a xml file containing the layout of the board
    """
    def __init__(self, xml_layout_document, interaction=False):
        self._color_key = (255, 0, 255)
        self.elements = {}
        self.interaction = interaction
        docxml = minidom.parse(xml_layout_document)

        window_board = docxml.firstChild
        window_board_childs = window_board.childNodes

        functions.erase_childs_end_of_line(window_board_childs)

        for element in window_board_childs:
            tag = element.tagName
            attr = element.getAttribute('type')
            
            _x_ = eval('functions.parse_' + tag + '_' + attr + '(element)')
            self.elements[element.getAttribute('name')] = _x_
        
        self.window_size = self.elements['window_size']
        self.window_title = self.elements['window_title']
        self.state = {'button_exit': 0, 'button_left_2': 0, 'button_left_1': 0,
                      'button_right_1': 0, 'button_right_2': 0}
        
        self.favicon = pygame.image.load(self.elements['favicon'])

        self.player_a = None
        self.player_b = None
        self.board = None
        self._static_background = None
        self._buttons_rects = None
        self.labels = None
        self.buttons = None

    def init(self, player_a, player_b, initial_board):
        """
        This function intialize the elements that cant be initialize on the
        __init__ function.

        """
        self.favicon = pygame.image.load(self.elements['favicon'])

        self.player_a = player_a
        self.player_b = player_b
        
        self.board = initial_board
        
        self._create_labels()
        self._create_buttons()
        
        self._static_background = self._get_static_surface()
        self._buttons_rects = self._generate_buttons_rects()

    def _create_labels(self): #
        """
        Generates the surfaces with the labels that contains the players names
        """
        players_names = self.elements['players_names']
        piece_size = players_names['inside_labels']['piece_size']
        label_a = pygame.image.load(players_names['names_background']).convert()
        label_b = pygame.image.load(players_names['names_background']).convert()

        piece_a = pygame.transform.scale(pygame.image.load(self.player_a[0]),
                                         piece_size)
        piece_b = pygame.transform.scale(pygame.image.load(self.player_b[0]),
                                         piece_size)

        name_font = pygame.font.Font(self.elements['font_type'], 22)

        name_a = name_font.render(self.player_a[1], 1,
                                  self.elements['font_color'])
        name_b = name_font.render(self.player_b[1], 1,
                                  self.elements['font_color'])

        piece_position = players_names['inside_labels']['piece_position']
        text_position = players_names['inside_labels']['name_position']
        label_a.blit(piece_a, piece_position)
        label_a.blit(name_a, text_position)
        
        label_b.blit(piece_b, piece_position)
        label_b.blit(name_b, text_position)

        self.labels = (label_a, label_b)

    def _create_buttons(self):
        """
        Create the surfaces for the buttons
        """
        action_btns = self.elements['action_buttons']
        btn_exit_pth = self.elements['exit_button']['exit_button_images']
        btn_left_2_pth = action_btns['first_button']['first_button_images']
        btn_left_1_pth = action_btns['second_button']['second_button_images']
        btn_right_1_pth = action_btns['third_button']['third_button_images']
        btn_right_2_pth = action_btns['fourth_button']['fourth_button_images']
        self.buttons = {}

        btn_exit_default = pygame.image.load(btn_exit_pth[0])
        btn_exit_above = pygame.image.load(btn_exit_pth[1])
        btn_exit_pressed = pygame.image.load(btn_exit_pth[2])
        self.buttons['button_exit'] = (btn_exit_default,
                                       btn_exit_above,
                                       btn_exit_pressed)
        
        btn_left_2_default = pygame.image.load(btn_left_2_pth[0])
        btn_left_2_above = pygame.image.load(btn_left_2_pth[1])
        btn_left_2_pressed = pygame.image.load(btn_left_2_pth[2])
        self.buttons['button_left_2'] = (btn_left_2_default,
                                         btn_left_2_above,
                                         btn_left_2_pressed)
        
        btn_left_1_default = pygame.image.load(btn_left_1_pth[0])
        btn_left_1_above = pygame.image.load(btn_left_1_pth[1])
        btn_left_1_pressed = pygame.image.load(btn_left_1_pth[2])
        self.buttons['button_left_1'] = (btn_left_1_default,
                                         btn_left_1_above,
                                         btn_left_1_pressed)
        
        btn_right_1_default = pygame.image.load(btn_right_1_pth[0])
        btn_right_1_above = pygame.image.load(btn_right_1_pth[1])
        btn_right_1_pressed = pygame.image.load(btn_right_1_pth[2])
        self.buttons['button_right_1'] = (btn_right_1_default,
                                          btn_right_1_above,
                                          btn_right_1_pressed)
        
        btn_right_2_default = pygame.image.load(btn_right_2_pth[0])
        btn_right_2_above = pygame.image.load(btn_right_2_pth[1])
        btn_right_2_pressed = pygame.image.load(btn_right_2_pth[2])
        self.buttons['button_right_2'] = (btn_right_2_default,
                                          btn_right_2_above,
                                          btn_right_2_pressed)
        
    def _draw_background(self):
        """
        Load the background image and convert it to pygame surface
        """
        return pygame.image.load(self.elements['background']).convert()
    
    def _draw_labels(self):
        """
        Generates the surfaces containing the names and pieces of
        the the players
        """
        players_names = self.elements['players_names']
        labels_size = players_names['names_size']
        label_a_pos = players_names['inside_labels']['label_A_position']
        label_b_pos = players_names['inside_labels']['label_B_position']
        
        labels = pygame.Surface(labels_size)
        labels.set_colorkey(self._color_key)
        labels.fill(self._color_key)
        
        labels.blit(self.labels[0], label_a_pos)
        labels.blit(self.labels[1], label_b_pos)

        return labels
    
    def _draw_exit_button(self):
        """
        Generate the surface for the exit button
        """
        return self.buttons['button_exit'][self.state['button_exit']]

    def _draw_buttons(self):
        """
        Returns the surface for the buttons
        """
        action_btns = self.elements['action_buttons']
        buttons_size = action_btns['action_buttons_size']
        button_1 = self.buttons['button_left_2'][self.state['button_left_2']]
        button_2 = self.buttons['button_left_1'][self.state['button_left_1']]
        button_3 = self.buttons['button_right_1'][self.state['button_right_1']]
        button_4 = self.buttons['button_right_2'][self.state['button_right_2']]
        
        buttons = []
        
        buttons.append((button_1,
                        action_btns['first_button']['first_button_position']))
        buttons.append((button_2,
                        action_btns['second_button']['second_button_position']))
        buttons.append((button_3,
                        action_btns['third_button']['third_button_position']))
        buttons.append((button_4,
                        action_btns['fourth_button']['fourth_button_position']))
        
        buttons_srfc = pygame.Surface(buttons_size)
        buttons_srfc.set_colorkey(self._color_key)
        buttons_srfc.fill(self._color_key)
        
        for button in buttons:
            buttons_srfc.blit(button[0], button[1])
            
        return buttons_srfc
        
    def change_board(self, board):
        """
        Update the board with a new state
        """
        self.board = board

    def get_board_position(self):
        """
        Get the origin of the board on the main surface.
        """
        return self.elements['board']['board_position']

    def get_favicon(self):
        """
        Get the surface of the favicon
        """
        return self.favicon

    def get_window_size(self):
        """
        Get the windows size
        """
        return self.window_size

    def get_window_title(self):
        """
        Get the windows title
        """
        return self.window_title

    def _get_absolute_position(self, pos1, pos2):
        """
        Get the position in an absolute way
        """
        return (pos1[0] + pos2[0], pos1[1] + pos2[1])

    def _generate_buttons_rects(self):
        """
        Generate the rects of the buttons to check collisions
        """
        surface = pygame.Surface(self.window_size)

        button_exit = self.buttons['button_exit'][0]
        if not self.interaction:
            button_1 = self.buttons['button_left_2'][0]
            button_2 = self.buttons['button_left_1'][0]
            button_3 = self.buttons['button_right_1'][0]
            button_4 = self.buttons['button_right_2'][0]

        exit_button_pos = self.elements['exit_button']['exit_button_position']

        if not self.interaction:
            action_btns = self.elements['action_buttons']
            action_buttons_pos = action_btns['action_buttons_position']
            
            temp = action_btns['first_button']['first_button_position']
            left_2_button_pos = temp
            left_2_button_pos = self._get_absolute_position(action_buttons_pos,
                                                            left_2_button_pos)

            temp = action_btns['second_button']['second_button_position']
            left_1_button_pos = temp
            left_1_button_pos = self._get_absolute_position(action_buttons_pos,
                                                            left_1_button_pos)

            temp = action_btns['third_button']['third_button_position']
            right_1_button_pos = temp
            right_1_button_pos = self._get_absolute_position(action_buttons_pos,
                                                             right_1_button_pos)

            temp = action_btns['fourth_button']['fourth_button_position']
            right_2_button_pos = temp
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
        """
        Get the buttons rects
        """
        return self._buttons_rects
        
    def _get_static_surface(self):
        """
        Generates and return the static surface.
        """
        label_position = self.elements['players_names']['names_position']
        
        back_surface = pygame.Surface(self.elements['window_size'])
        
        background = self._draw_background()
        labels = self._draw_labels()
        
        back_surface.blit(background, (0, 0))
        back_surface.blit(labels, label_position)

        return back_surface

    def get_surface(self, mouse = None):
        """
        Return the entire pygame surface with all the display
        """
        exit_position = self.elements['exit_button']['exit_button_position']
        action_btns = self.elements['action_buttons']
        buttons_position = action_btns['action_buttons_position']
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

        final_surface.blit(self._static_background, (0, 0))
        final_surface.blit(self.board, board_position)
        final_surface.blit(exit_button, exit_position)
        if not self.interaction:
            final_surface.blit(buttons, buttons_position)

        return final_surface
