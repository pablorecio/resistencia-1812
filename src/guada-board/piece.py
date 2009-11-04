# -*- coding: utf-8 -*-

import pygame
import pygame.font

class Piece(object):
    """
    @brief This class provides a simple abstraction layer for the pieces on the board.
    It is a simple class, you only have to create the object and you can get a drawdable
    surface with the piece and the number with its value.
    """
    def __init__(self, value = 0, covered = 0, size = 60,
                 img_path = './images/piece-default.png',
                 font = './fonts/LiberationMono-Bold.ttf'):
        """
        @brief Init method for the class <i>Piece</i>. This method simply initialize
        the values properly
        @param self The actual object that calls this method
        @param value Piece numeric value. This value determines the strength of the
        piece. But here doesn't matter this, it's only the value putted on the piece
        @param covered Integer that shows if the piece is covered (0) or uncovered (1)
        @param size Size of the tile.
        @param img_path Path to the piece image.
        """

        self.value = value
        self.img_path = img_path
        self.size = size
        self.covered = covered
        self.font = font

    def get_value(self):
        """
        Getter for the numeric value of the piece.
        @return Integer with the numeric value of the piece.
        """
        return self.value;

    def get_size(self):
        """
        Getter for the size of the piece
        @return Integer with the size of the piece
        """
        return self.size;

    def get_surface(self):
        """
        This method generate a surface drawdable with the piece and its value.
        @return A pygame surface with the piece and the value.
        """
        image = pygame.image.load(self.img_path).convert()
        size = (self.size,)*2 #This gives a pair (self.size, self.size)


        surface = pygame.Surface(size).convert()
        surface.blit(image,(0,0))

        if self.value != 0:
        
            color = (255,)*3 #White
            border_color = (0,)*3 #Black
        
            border = pygame.font.Font(self.font, 34)
            insider = pygame.font.Font(self.font, 32)

            if self.covered == 0:
                border_text = border.render('['+str(self.value)+']', 1, border_color)
                insider_text = insider.render('['+str(self.value)+']', 1, color)
            else:
                border_text = border.render(str(self.value), 1, border_color)
                insider_text = insider.render(str(self.value), 1, color)
        
            textpos = insider_text.get_rect(centerx=surface.get_width()/2, centery=surface.get_width()/2)
            
            surface.blit(border_text,textpos)
            surface.blit(insider_text,textpos)

        return surface

    
        
