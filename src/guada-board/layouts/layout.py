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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
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

import xml_layout_functions as functions

# To clarify this, here is a little schema of the list 'self.elements'
# after reading the XML file:
#
# - 'title'
# - 'background'
# - 'favicon'
# - 'font_type'
# - 'font_syze'
# - 'font_color'
# - 'window_syze'
# - 'board'
#   |- 'board_size'
#   |- 'board_position'
# - 'players_names'
#   |- 'names_background'
#   |- 'names_size'
#   |- 'names_position'
#   |- 'inside_Labels'
#      |- 'piece_position'
#      |- 'name_position'
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
    def __init__(self, xml_layout_document):
        self.elements = {}
        docxml = minidom.parse(xml_layout_document)

        window_board = docxml.firstChild
        window_board_childs = window_board.childNodes

        functions.erase_childs_end_of_line(window_board_childs)

        for element in window_board_childs:
            tag = element.tagName
            attr = element.getAttribute('type')
            
            x = eval('functions.parse_' + tag + '_' + attr + '(element)')
            self.elements[element.getAttribute('name')] = x


        self.background = pygame.image.load(self.elements['background'])
        self.background.convert()

        self.font = pygame.font.Font(self.elements['font_type'],22)

        #self.favicon =

        self.font_color = self.elements['font_color']

        self.window_size = self.elements['window_size']

        self.board = self.elements['board']

    def get_surface(self):
        return self.background
