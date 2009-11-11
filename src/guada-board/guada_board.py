
# -*- coding: utf-8 -*-

import pygame
import board

import sys
sys.path.append("./libguadalete")
import libguadalete
import game

screen_size = (760,560)
board_ub = (10,10)

def run(teamA, teamB):
    print teamA
    print teamB
    lib = libguadalete.LibGuadalete(teamA,teamB)
    out_file = lib.run_game()

    entire_game = lib.parseFile(out_file)
    
    pygame.init()

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Resistencia en Cadiz: 1812 (Tablero)')
    favicon = pygame.image.load('images/favicon.png').convert()
    pygame.display.set_icon(favicon)

    res_game = game.Game(entire_game, './images/piece-orange.png',
                         './images/piece-violete.png',
                         './images/piece-default.png')

    background = pygame.image.load('images/fondo.png').convert()
    img_board = res_game.draw_board().convert()

    screen.blit(background,(0,0))
    screen.blit(img_board,board_ub)
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
                    screen.blit(background,(0,0))
                    screen.blit(surface,board_ub)
                    pygame.display.flip()
                if event.key == 276:
                    res_game.previous_turn()
                    surface = res_game.draw_board()
                    surface.convert()
                    screen.blit(background,(0,0))
                    screen.blit(surface,board_ub)
                    pygame.display.flip()
