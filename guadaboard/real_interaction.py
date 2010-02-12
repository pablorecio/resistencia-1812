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

import os.path
import time

import gtk

import dyn_game

from libguadalete import file_parser
from resistencia import xdg
from resistencia.gui import notify_result

#path_file = 'temporal.txt'
        
        
def _find_element_matrix(board, e):
    """
    Check the existence of the element on a matrix.
    """
    sum = 0
    for l in board:
        sum += l.count(e)

    return not sum == 0

def _define_winner(board):
    """
    Checking the last board of a game, determines the result.
    Will return 0 if it's a draw, 1 if the first team won and
    -1 if the second team won.
    """
    king_A = _find_element_matrix(board, 1)
    king_B = _find_element_matrix(board, -1)
    print king_A
    print king_B

    if (king_A and king_B) or (not king_A and not king_B):
        return 0
    elif king_A:
        return 1
    else:
        return -1

class HumanInteraction:
    def __init__(self, teamA, teamB, default_piece, player,
                 number_turns):
        self.teamA = teamA[0]
        self.teamB = teamB[0]
        self.number_turns = number_turns
        self.game_interaction = dyn_game.DynGame(teamA, teamB,
                                                 default_piece,
                                                 xml_file= xdg.get_data_path('layouts/main-layout.xml'),
                                                 player=player)

    def update_games(self):
        if os.path.exists('temporal.txt'):
            path_file = 'temporal.txt'
        else:
            path_file = 'resultado.txt'
        games = file_parser.parse_temp_file(path_file)

        turns_parsed = len(games)
        turns_played = self.game_interaction.get_number_of_turns()
        diff = turns_parsed - turns_played
        
        new_turns = games[len(games) - diff:]
        self.last_turn = games[len(games) - 1]
        self.num_turns_played = turns_played
        self.last_movement = self.game_interaction.draw_boards(new_turns)

    def finish(self):
        self.update_games()
        time.sleep(3)
        self.game_interaction.finish()
        show_dialog_result((self.teamA, self.teamB), self.define_winner())
        

    def get_identifier_last_move(self):
        print 'get_identifier_last_move'
        self.update_games()
        return self.last_movement[0]

    def get_movement_last_move(self):
        print 'get_movement_last_move'
        return self.last_movement[1]

    def define_winner(self):
        return _define_winner(self.last_turn[0])

def show_dialog_result((name_teamA, name_teamB), winner):
    n = notify_result.notifyResult((name_teamA, name_teamB), winner)
    n.dlg_result.run()
        
    while gtk.events_pending():
        gtk.main_iteration(False)
