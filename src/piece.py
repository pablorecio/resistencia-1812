# -*- coding: utf-8 -*-

import pygame
import pygame.font

class Piece(object):
    """
    @brief This class provides a simple abstraction layer for the pieces on the board.
    It is a simple class, you only have to create the object and you can get a drawdable
    surface with the piece and the number with its value.
    """
    def __init__(self, value = 0, team = 0, size = 60, img_path = './images/piece-default.png',
                 font = './fonts/LiberationMono-Bold.ttf'):
        """
        @brief Init method for the class <i>Piece</i>. This method simply initialize
        the values properly
        @param self The actual object that calls this method
        @param value Piece numeric value. This value determines the strength of the
        piece. But here doesn't matter this, it's only the value putted on the piece
        @param team Integer with the team that owns this piece. It can be 0 if there is
        no team (so it will be a default piece), 1 or -1. No more values allowed
        @param size Size of the tile.
        @param img_path Path to the piece image.
        """
        assert (team >= -1 and team <= 1), 'Failed to load piece. Team value not allowed'

        self.value = value
        self.img_path = img_path
        self.size = size
        self.team = team
        self.font = font

        self.key = value * ((-1)**(team+1)) 

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

    def get_key(self):
        """
        This method gets te key of this piece. The key is builded in
        the initialization:
        <li>0 if it's a default piece</li>
        <li><i>value</i> if it's a piece of the team A</li>
        <li>-<i>value</i> if it's a piece of the team B</li>
        @return An integer with the key of this piece
        """
        return self.key;
        

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
        
            border = pygame.font.Font(self.font, 44)
            insider = pygame.font.Font(self.font, 40)
        
            border_text = border.render(str(self.value), 1, border_color)
            insider_text = insider.render(str(self.value), 1, color)
        
            textpos = insider_text.get_rect(centerx=surface.get_width()/2, centery=surface.get_width()/2)
            
            surface.blit(border_text,textpos)
            surface.blit(insider_text,textpos)

        return surface

    
        
