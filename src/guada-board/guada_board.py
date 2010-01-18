
# -*- coding: utf-8 -*-

import pygame
import pygame.font
import board

import os
from os import path
import sys
sys.path.append("./libguadalete")
sys.path.append("./guada-board/layouts")
import libguadalete
import file_parser
import layout
import game

def _load_game_from_file(src_file, teamA, teamB, path_piece_default, xml_file):
    entire_game, winner = file_parser.parse_file(src_file)

    if winner == 0:
        print 'Empate'
    elif winner == 1:
        print 'Ganó ' + teamA[0]
    else:        
        print 'Ganó ' + teamB[0]

    
    pygame.init()

    background_surfaces = {}

    xml_layout = layout.Layout(xml_file)
    
    screen = pygame.display.set_mode(xml_layout.get_window_size())
    pygame.display.set_caption(xml_layout.get_window_title())

    res_game = game.Game(entire_game, teamA[1],
                         teamB[1], path_piece_default)

    img_board = res_game.draw_board().convert()
    
    xml_layout.init((teamA[1], teamA[0]), (teamB[1], teamB[0]), img_board)
    rects = xml_layout.get_buttons_rects()
    
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

def extract_name(team):
    i = team[0].find("/reglas")
    j = team[0].find(".clp")

    return (team[0])[i+7:j]

def extract_names_from_file(src_file):
    useless, file_name = path.split(src_file)

    nameA_i = 20
    nameA_j = file_name.find('-vs-')
    nameB_i = nameA_j + 4
    nameB_j = file_name.find('.txt')

    return (file_name[nameA_i:nameA_j], file_name[nameB_i:nameB_j])

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

def run(teamA, teamB, fast = False, dont_log = False, path_piece_default='./images/piece-default.png', xml_file='./guada-board/layouts/xml_prueba.xml'):
    lib = libguadalete.LibGuadalete(teamA[0],teamB[0])
    out_file, winner = lib.run_game()
    if not fast:
        name_team_A = extract_name(teamA[0])
        name_team_B = extract_name(teamB[0])
        _load_game_from_file(out_file, (name_team_A, teamA[1]),
                             (name_team_B, teamB[1]), path_piece_default, xml_file)
    if dont_log:
        os.remove(out_file)
    return winner

def run_from_file(src_file,
                  teamA=('equipoA', './images/piece-orange.png'),
                  teamB=('equipoB', './images/piece-violete.png'),
                  path_piece_default='./images/piece-default.png',
                  xml_file='./guada-board/layouts/xml_prueba.xml'):
    nameA, nameB = extract_names_from_file(src_file)
    teamA = (nameA, teamA[1])
    teamB = (nameB, teamB[1])
    _load_game_from_file(src_file, teamA, teamB, path_piece_default, xml_file)

    
