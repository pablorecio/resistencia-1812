# -*- coding: utf-8 -*-

import pygame

class Button(object):
    def __init__(self, images): #check the same size of the images
        print images
        self.img_default = pygame.image.load(images[0])
        self.img_above = pygame.image.load(images[1])
        self.img_pressed = pygame.image.load(images[2])

        self.size = self.img_default.get_size()

    def get_size(self):
        return self.size

    def get_width(self):
        return self.size[0]

    def get_height(self):
        return self.size[1]

    def get_surface(self, state):
        if state == 0:
            return self.img_default
        elif state == 1:
            return self.img_above
        elif state == 2:
            return self.img_pressed

    def get_default_surface(self):
        return self.img_default

    def get_above_surface(self):
        return self.img_above

    def get_pressed_surface(self):
        return self.img_pressed
