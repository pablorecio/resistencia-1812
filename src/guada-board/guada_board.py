
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

def get_collision(point, rects):
    res = ''
    for index in rects:
        rect = rects[index]
        if rect.collidepoint(point):
            res = index
            break

    return res

def _get_turn(game, xml_layout, mouse=None):
    surface = game.draw_board()
    surface.convert()
    xml_layout.change_board(surface)

    return xml_layout.get_surface(mouse)

def next_turn(game, xml_layout, mouse=None):
    game.next_turn()
    return _get_turn(game, xml_layout, mouse)

def previous_turn(game, xml_layout, mouse=None):
    game.previous_turn()
    return _get_turn(game, xml_layout, mouse)

def first_turn(game, xml_layout, mouse=None):
    game.first_turn()
    return _get_turn(game, xml_layout, mouse)

def last_turn(game, xml_layout, mouse=None):
    game.last_turn()
    return _get_turn(game, xml_layout, mouse)

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
    rects = xml_layout.get_buttons_rects()

    print rects
    
    pygame.display.set_icon(xml_layout.get_favicon())

    screen.blit(xml_layout.get_surface(),(0,0))
    pygame.display.flip()

    band_pos = False
    clock = pygame.time.Clock()
    while True:
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return 
            elif event.type == pygame.KEYDOWN:
                if event.key == 275:
                    surface = next_turn(res_game, xml_layout)
                    screen.blit(surface,(0,0))
                    pygame.display.flip()
                if event.key == 276:
                    surface = previous_turn(res_game, xml_layout)
                    screen.blit(surface,(0,0))
                    pygame.display.flip()
            elif event.type == pygame.MOUSEMOTION:
                res = get_collision(event.pos, rects)
                if res != '':
                    if band_pos == False:
                        surface = xml_layout.get_surface((res,2))
                        screen.blit(surface,(0,0))
                        pygame.display.flip()                        
                        band_pos = True
                else:
                    if band_pos == True:
                        surface = xml_layout.get_surface()
                        screen.blit(surface,(0,0))
                        pygame.display.flip()
                        band_pos = False
            elif event.type == pygame.MOUSEBUTTONUP:
                res = get_collision(event.pos, rects)
                if event.button == 1 and res != '':
                    if res == 'button_exit':
                        pygame.display.quit()
                        return
                    else:
                        if res == 'button_left_2':
                            surface = first_turn(res_game, xml_layout, (res, 1))
                            screen.blit(surface,(0,0))
                            pygame.display.flip()
                        elif res == 'button_left_1':
                            surface = previous_turn(res_game, xml_layout, (res, 1))
                            screen.blit(surface,(0,0))
                            pygame.display.flip()
                        elif res == 'button_right_1':
                            surface = next_turn(res_game, xml_layout, (res, 1))
                            screen.blit(surface,(0,0))
                            pygame.display.flip()
                        elif res == 'button_right_2':
                            surface = last_turn(res_game, xml_layout, (res, 1))
                            screen.blit(surface,(0,0))
                            pygame.display.flip()
