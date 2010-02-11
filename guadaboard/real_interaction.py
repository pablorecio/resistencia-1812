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

import dyn_game

from libguadalete import file_parser
from resistencia import xdg

path_file = 'temporal.txt'

class HumanInteraction:
    def __init__(self, teamA, teamB, default_piece, player,
                 number_turns):
        self.number_turns = number_turns
        self.game_interaction = dyn_game.DynGame(teamA, teamB,
                                                 default_piece,
                                                 xml_file= xdg.get_data_path('layouts/main-layout.xml'),
                                                 player=player)

    def update_games(self):
        print 'update_games'
        games = file_parser.parse_temp_file(path_file)

        turns_parsed = len(games)
        turns_played = self.game_interaction.get_number_of_turns()
        diff = turns_parsed - turns_played
        
        new_turns = games[len(games) - 2:]
        self.last_movement = self.game_interaction.draw_boards(new_turns)

    def get_identifier_last_move(self):
        print 'get_identifier_last_move'
        self.update_games()
        return self.last_movement[0]

    def get_movement_last_move(self):
        print 'get_movement_last_move'
        return self.last_movement[1]
        
