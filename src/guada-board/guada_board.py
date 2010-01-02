
# -*- coding: utf-8 -*-

import pygame
import pygame.font
import board

import sys
sys.path.append("./libguadalete")
sys.path.append("./guada-board/layouts")
import libguadalete
import layout
import game


def extract_name(team):
    i = team[0].find("/reglas")
    j = team[0].find(".clp")

    return (team[0])[i+7:j]

def run(teamA, teamB, path_piece_default='./images/piece-default.png', xml_file='./guada-board/layouts/xml_prueba.xml'):
    lib = libguadalete.LibGuadalete(teamA[0],teamB[0])
    out_file = lib.run_game()

    entire_game = lib.parseFile(out_file)
    
    pygame.init()

    background_surfaces = {}
    name_team_A = extract_name(teamA[0])
    name_team_B = extract_name(teamB[0])

    xml_layout = layout.Layout(xml_file)
    
    screen = pygame.display.set_mode(xml_layout.get_window_size())
    pygame.display.set_caption(xml_layout.get_window_title())

    res_game = game.Game(entire_game, teamA[1],
                         teamB[1], path_piece_default)

    img_board = res_game.draw_board().convert()
    
    xml_layout.init((teamA[1], name_team_A), (teamB[1], name_team_B), img_board)
    
    pygame.display.set_icon(xml_layout.get_favicon())

    screen.blit(xml_layout.get_surface(),(0,0))
    pygame.display.flip()

    clock = pygame.time.Clock()
    while True:
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return 
            elif event.type == pygame.KEYDOWN:
                if event.key == 275:
                    res_game.next_turn()
                    surface = res_game.draw_board()
                    surface.convert()
                    xml_layout.change_board(surface)
                    screen.blit(xml_layout.get_surface(),(0,0))
                    pygame.display.flip()
                if event.key == 276:
                    res_game.previous_turn()
                    surface = res_game.draw_board()
                    surface.convert()
                    xml_layout.change_board(surface)
                    screen.blit(xml_layout.get_surface(),(0,0))
                    pygame.display.flip()
            elif event.type == pygame.MOUSEMOTION:
                print event.pos
