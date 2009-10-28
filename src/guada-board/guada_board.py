# -*- coding: utf-8 -*-

import pygame
import board

import sys
sys.path.append("./libguadalete")
import libguadalete
import game

def run(teamA, teamB):
    print teamA
    print teamB
    lib = libguadalete.LibGuadalete(teamA,teamB)
    out_file = lib.run_game()

    entire_game = lib.parseFile(out_file)
    
    pygame.init()

    screen = pygame.display.set_mode((480,480))
    pygame.display.set_caption('Resistencia en Cadiz: 1812 (Tablero)')
    favicon = pygame.image.load('images/favicon.png').convert()
    pygame.display.set_icon(favicon)

    res_game = game.Game(entire_game, './images/piece-orange.png',
                         './images/piece-violete.png',
                         './images/piece-default.png')

    background = res_game.draw_board().convert()

    screen.blit(background,(0,0))
    pygame.display.flip()

    clock = pygame.time.Clock()
    while True:
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return 
            if event.type == pygame.KEYDOWN:
                if event.key == 275:
                    res_game.next_turn()
                    surface = res_game.draw_board()
                    surface.convert()
                    screen.blit(surface,(0,0))
                    pygame.display.flip()
                if event.key == 276:
                    res_game.previous_turn()
                    surface = res_game.draw_board()
                    surface.convert()
                    screen.blit(surface,(0,0))
                    pygame.display.flip()
