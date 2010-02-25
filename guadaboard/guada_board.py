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
Main module that handle the representation of a entire game
"""

import os

import pygame
import pygame.font
import pygame.mixer

import gtk

from libguadalete import libguadalete, file_parser, stats
from libguadalete.libguadalete import FileError as LibFileError
from resistencia import filenames, xdg, configure
from resistencia.gui import notify_result
import guadaboard.game as game
import guadaboard.layout as layout

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class GuadaFileError(Error):
    """
    Exception to handle the error parsing a file
    """
    def __init__(self, msg):
        self.msg = msg

def _handle_draw(output_file):
    """
    Handle the draw if the game cant draw
    """
    entire_game, winner = file_parser.parse_file(output_file)

    if not winner == 0:
        return winner
    else: #if it's a draw
        num_a = 0
        num_b = 0
        _sum = 0
        final_board = entire_game[len(entire_game) - 1]
        _num = len(final_board)
        for i in range(_num):
            for j in range(_num):
                _value = final_board[i][j]
                _sum = _sum + _value
                if not _value == 0:
                    if _value > 0:
                        num_a = num_a + 1
                    else:
                        num_b = num_b + 1
        if not _sum == 0: #a team has more _sum of values than the other
            if _sum > 0:
                return 1
            else:
                return -1
        else: #both has the same _sum of values
            if not num_a == num_b: #a team has more pieces than the other
                if num_a > num_b:
                    return 1
                else:
                    return -1
            else: #both have the same number of pieces. 
                return -1 #B team is in disvantage
            

def _load_game_from_file(src_file, team_a, team_b, path_piece_def, xml_file,
                         hidden=False, cant_draw=False):
    entire_game, winner = file_parser.parse_file(src_file)
    if cant_draw:
        winner = _handle_draw(src_file)

    if winner == 0:
        print 'Empate'
    elif winner == 1:
        print 'Ganó ' + team_a[0]
    else:        
        print 'Ganó ' + team_b[0]

    music = False
    if configure.load_configuration()['music_active'] == '1':
        music = True
    
    pygame.init()

    xml_layout = layout.Layout(xml_file)
    
    screen = pygame.display.set_mode(xml_layout.get_window_size())
    pygame.display.set_caption(xml_layout.get_window_title())

    if music:
        _music_path = xdg.get_data_path('music/walking_on_old_stones.ogg')
        pygame.mixer.music.load(_music_path)
        pygame.mixer.music.play()

    res_game = game.Game(entire_game, team_a[1],
                         team_b[1], path_piece_def,hidden=hidden)

    img_board = res_game.draw_board().convert()
    
    xml_layout.init((team_a[1], team_a[0]), (team_b[1], team_b[0]), img_board)
    rects = xml_layout.get_buttons_rects()
    
    pygame.display.set_icon(xml_layout.get_favicon())

    screen.blit(xml_layout.get_surface(), (0, 0))
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
                show_dialog_result((team_a[0], team_b[0]), winner)
                return winner
            elif event.type == pygame.KEYDOWN:
                if event.key == 275:
                    surface = next_turn(res_game, xml_layout)
                    screen.blit(surface, (0, 0))
                    pygame.display.flip()
                if event.key == 276:
                    surface = previous_turn(res_game, xml_layout)
                    screen.blit(surface, (0, 0))
                    pygame.display.flip()
            elif event.type == pygame.MOUSEMOTION:
                res = get_collision(event.pos, rects)
                if res != '':
                    if band_pos == False:
                        surface = xml_layout.get_surface((res, 2))
                        screen.blit(surface, (0, 0))
                        pygame.display.flip()                        
                        band_pos = True
                else:
                    if band_pos == True:
                        surface = xml_layout.get_surface()
                        screen.blit(surface, (0, 0))
                        pygame.display.flip()
                        band_pos = False
            elif event.type == pygame.MOUSEBUTTONUP:
                res = get_collision(event.pos, rects)
                if event.button == 1 and res != '':
                    if res == 'button_exit':
                        if music:
                            pygame.mixer.music.stop()
                        pygame.display.quit()
                        show_dialog_result((team_a[0], team_b[0]), winner)
                        return winner
                    else:
                        if res == 'button_left_2':
                            surface = first_turn(res_game, xml_layout, (res, 1))
                            screen.blit(surface, (0, 0))
                            pygame.display.flip()
                        elif res == 'button_left_1':
                            surface = previous_turn(res_game,
                                                    xml_layout, (res, 1))
                            screen.blit(surface, (0, 0))
                            pygame.display.flip()
                        elif res == 'button_right_1':
                            surface = next_turn(res_game, xml_layout, (res, 1))
                            screen.blit(surface, (0, 0))
                            pygame.display.flip()
                        elif res == 'button_right_2':
                            surface = last_turn(res_game, xml_layout, (res, 1))
                            screen.blit(surface, (0, 0))
                            pygame.display.flip()

def get_collision(point, rects):
    """
    Function that checks if it is a collision with the buttons
    """
    res = ''
    for index in rects:
        rect = rects[index]
        if rect.collidepoint(point):
            res = index
            break

    return res

def _get_turn(actual_game, xml_layout, mouse=None):
    """
    Changes the turn
    """
    surface = actual_game.draw_board()
    surface.convert()
    xml_layout.change_board(surface)

    return xml_layout.get_surface(mouse)

def next_turn(actual_game, xml_layout, mouse=None):
    """
    Iterates to the next turn
    """
    actual_game.next_turn()
    return _get_turn(actual_game, xml_layout, mouse)

def previous_turn(actual_game, xml_layout, mouse=None):
    """
    Iterates to the previous turn
    """
    actual_game.previous_turn()
    return _get_turn(actual_game, xml_layout, mouse)

def first_turn(actual_game, xml_layout, mouse=None):
    """
    Iterates to the first turn
    """
    actual_game.first_turn()
    return _get_turn(actual_game, xml_layout, mouse)

def last_turn(actual_game, xml_layout, mouse=None):
    """
    Iterates to the last turn
    """
    actual_game.last_turn()
    return _get_turn(actual_game, xml_layout, mouse)

def run(team_a, team_b, fast=False, dont_log=False, hidden=False,
        number_turns=100, 
        path_piece_def= xdg.get_data_path('images/piece-default.png'),
        xml_file= xdg.get_data_path('layouts/main-layout.xml'),
        get_stats=False, cant_draw=False):
    """
    Runs a game using the system expert teams given. It calls to libguadalete,
    generating the game and parsing the file.
    """
    lib = libguadalete.LibGuadalete(team_a[0], team_b[0], number_turns)
    try:
        out_file, winner = lib.run_game()
    except LibFileError as exc:
        raise GuadaFileError(exc.msg)
    if not fast:
        name_team_a = filenames.extract_name_expert_system(team_a[0])
        name_team_b = filenames.extract_name_expert_system(team_b[0])
        _load_game_from_file(out_file, (name_team_a, team_a[1]),
                             (name_team_b, team_b[1]), path_piece_def,
                             xml_file, hidden, cant_draw=cant_draw)
    if cant_draw:
        winner = _handle_draw(out_file)
    res = winner
    if get_stats:
        res = (winner, stats.get_game_file_stats(out_file))
    if dont_log or get_stats:
        os.remove(out_file)
    return res

def run_from_file(src_file,
                  team_a=('equipoA',
                         xdg.get_data_path('images/piece-orange.png')),
                  team_b=('equipoB',
                         xdg.get_data_path('images/piece-violete.png')),
                  path_piece_def=xdg.get_data_path('images/piece-default.png'),
                  xml_file=xdg.get_data_path('layouts/alternative-layout.xml')):
    """
    Run a game directly from a file, not simulating a game.
    """
    name_a, name_b = filenames.extract_names_from_file(src_file)
    team_a = (name_a, team_a[1])
    team_b = (name_b, team_b[1])
    winner = _load_game_from_file(src_file, team_a, team_b,
                                  path_piece_def, xml_file)

    return winner

def show_dialog_result((name_team_a, name_team_b), winner):
    """
    Simple function that show a dialog with the result of a game
    """
    _not_dig = notify_result.notifyResult((name_team_a, name_team_b), winner)
    _not_dig.dlg_result.run()
        
    while gtk.events_pending():
        gtk.main_iteration(False)
