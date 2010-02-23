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
This module is the middle layer between the kernel of a one player game and its
representation on pygame.
"""

import os.path
import time

import gtk

from guadaboard import dyn_game

from libguadalete import file_parser
from resistencia import xdg
from resistencia.gui import notify_result

#path_file = 'temporal.txt'
__default_layout__ = xdg.get_data_path('layouts/main-layout.xml')
        
def _find_element_matrix(board, element):
    """
    Check the existence of the element on a matrix.
    """
    _sum = 0
    for line in board:
        _sum += line.count(element)

    return not _sum == 0

def _define_winner(board):
    """
    Checking the last board of a game, determines the result.
    Will return 0 if it's a draw, 1 if the first team won and
    -1 if the second team won.
    """
    king_a = _find_element_matrix(board, 1)
    king_b = _find_element_matrix(board, -1)
    print king_a
    print king_b

    if (king_a and king_b) or (not king_a and not king_b):
        return 0
    elif king_a:
        return 1
    else:
        return -1

class HumanInteraction:
    """
    Class that models...
    """
    def __init__(self, team_a, team_b, default_piece, player,
                 number_turns):
        self.team_a = team_a[0]
        self.team_b = team_b[0]
        self.number_turns = number_turns
        self.last_turn = 0
        self.num_turns_played = 0
        self.last_movement = 0
        self.game_interaction = dyn_game.DynGame(team_a, team_b,
                                                 default_piece,
                                                 xml_file=__default_layout__,
                                                 player=player)

    def update_games(self):
        """
        Updates the games. Read the temp file, so we add to the display the
        newest boards
        """
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
        """
        Close the environment
        """
        self.update_games()
        time.sleep(3)
        self.game_interaction.finish()
        show_dialog_result((self.team_a, self.team_b), self.define_winner())
        

    def get_identifier_last_move(self):
        """
        Get the id of the last move
        """
        print 'get_identifier_last_move'
        self.update_games()
        return self.last_movement[0]

    def get_movement_last_move(self):
        """
        Get the movement did on the last move
        """
        print 'get_movement_last_move'
        return self.last_movement[1]

    def define_winner(self):
        """
        Function used to define who wons
        """
        return _define_winner(self.last_turn[0])

def show_dialog_result((name_team_a, name_team_b), winner):
    """
    Simple function that show a dialog with the result of a game
    """
    not_dig = notify_result.notifyResult((name_team_a, name_team_b), winner)
    not_dig.dlg_result.run()
        
    while gtk.events_pending():
        gtk.main_iteration(False)
