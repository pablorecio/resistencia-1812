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
This module provides the class Piece, who draws a piece for the board
representation.
"""

import pygame
import pygame.font

from resistencia import xdg


class Piece(object):
    """This class provides an abstraction layer for the pieces on the board.

    It is a simple class, you only have to create the object and you
    can get a drawdable surface with the piece and the number with its value.
    """
    def __init__(self, value=0, covered=0, size=60, hidden=False,
                 img_path=xdg.get_data_path('images/piece-default.png'),
                 font=xdg.get_data_path('fonts/LiberationMono-Bold.ttf')):
        """Init method for the class Piece

        Keyword arguments:
        value -- Piece numeric value. This value determines the strength
        of the piece. But here doesn't matter this, it's only the value
        putted on the piece
        covered -- Integer that shows if the piece is covered (0)
        or uncovered (1)
        size -- Size of the tile.
        img_path -- Path to the piece image.
        font -- Path to the font file that will be use to render
        the number.
        """

        self.value = value
        self.img_path = img_path
        self.size = size
        self.covered = covered
        self.hidden = hidden
        self.font = font

    def get_value(self):
        """
        Getter for the numeric value of the piece.
        """
        return self.value

    def get_size(self):
        """
        Getter for the size of the piece
        """
        return self.size

    def get_surface(self):
        """This method generate a surface drawdable with the piece and
        its value.

        Return a pygame.surface with the complete piece draw.
        """
        image = pygame.image.load(self.img_path).convert()
        size = (self.size, ) * 2  # This gives a pair (self.size, self.size)

        surface = pygame.Surface(size).convert()
        surface.blit(image, (0, 0))

        if self.value != 0:

            color = (255, ) * 3  # White
            border_color = (0, ) * 3  # Black

            border = pygame.font.Font(self.font, 34)
            insider = pygame.font.Font(self.font, 32)

            if self.covered == 0:
                if not self.hidden:
                    border_text = border.render(
                        "[%d]" % self.value, 1, border_color)
                    insider_text = insider.render(
                        "[%d]" % self.value, 1, color)
            else:
                border_text = border.render(
                    "%d" % self.value, 1, border_color)
                insider_text = insider.render(
                    "%d" % self.value, 1, color)

            if not (self.covered == 0 and self.hidden):
                textpos = insider_text.get_rect(
                    centerx=surface.get_width() / 2,
                    centery=surface.get_width() / 2)

                surface.blit(border_text, textpos)
                surface.blit(insider_text, textpos)

        return surface
