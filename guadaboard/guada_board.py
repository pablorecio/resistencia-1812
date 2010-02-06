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

import os
from os import path
import sys

import pygame
import pygame.font
import pygame.mixer

from libguadalete import libguadalete, file_parser, stats
from libguadalete.libguadalete import FileError as LibFileError
from resistencia import filenames, xdg, configure
from resistencia.gui import notify_result
import game
import layout

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class GuadaFileError(Error):
    def __init__(self, msg):
        self.msg = msg

def _load_game_from_file(src_file, teamA, teamB, path_piece_default, xml_file,
                         hidden=False):
    entire_game, winner = file_parser.parse_file(src_file)

    if winner == 0:
        print 'Empate'
    elif winner == 1:
        print 'Ganó ' + teamA[0]
    else:        
        print 'Ganó ' + teamB[0]

    music = False
    if configure.load_configuration()['music_active'] == '1':
        music = True
    
    pygame.init()

    background_surfaces = {}
    xml_layout = layout.Layout(xml_file)
    
    screen = pygame.display.set_mode(xml_layout.get_window_size())
    pygame.display.set_caption(xml_layout.get_window_title())

    if music:
        pygame.mixer.music.load(xdg.get_data_path('music/walking_on_old_stones.ogg'))
        pygame.mixer.music.play()

    res_game = game.Game(entire_game, teamA[1],
                         teamB[1], path_piece_default,hidden=hidden)

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
                if music:
                    pygame.mixer.music.stop()
                pygame.display.quit()
                show_dialog_result((teamA[0], teamB[0]), winner)
                return winner
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
                        if music:
                            pygame.mixer.music.stop()
                        pygame.display.quit()
                        show_dialog_result((teamA[0], teamB[0]), winner)
                        return winner
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

def run(teamA, teamB, fast=False, dont_log=False, hidden=False,
        number_turns=100, 
        path_piece_default= xdg.get_data_path('images/piece-default.png'),
        xml_file= xdg.get_data_path('layouts/main-layout.xml'), get_stats=False):
    lib = libguadalete.LibGuadalete(teamA[0],teamB[0],number_turns)
    try:
        out_file, winner = lib.run_game()
    except LibFileError as e:
        raise GuadaFileError(e.msg)
    if not fast:
        name_team_A = filenames.extract_name_expert_system(teamA[0])
        name_team_B = filenames.extract_name_expert_system(teamB[0])
        _load_game_from_file(out_file, (name_team_A, teamA[1]),
                             (name_team_B, teamB[1]), path_piece_default,
                             xml_file, hidden)
    res = winner
    if get_stats:
        res = (winner, stats.get_game_file_stats(out_file))
    if dont_log or get_stats:
        os.remove(out_file)
    return res

def run_from_file(src_file,
                  teamA=('equipoA',
                         xdg.get_data_path('images/piece-orange.png')),
                  teamB=('equipoB',
                         xdg.get_data_path('images/piece-violete.png')),
                  path_piece_default= xdg.get_data_path('images/piece-default.png'),
                  xml_file= xdg.get_data_path('layouts/main-layout.xml')):
    nameA, nameB = filenames.extract_names_from_file(src_file)
    teamA = (nameA, teamA[1])
    teamB = (nameB, teamB[1])
    winner = _load_game_from_file(src_file, teamA, teamB, path_piece_default, xml_file)

    return winner

def show_dialog_result((name_teamA, name_teamB), winner):
    n = notify_result.notifyResult((name_teamA, name_teamB), winner)
    n.dlg_result.run()
