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
#               2007, Manuel Palomo Duarte, <manuel.palomo@uca.es>            #
###############################################################################

"""
This file contains the definition of the class LibGuadalete, main class that
wraps the behaviour of the game 'La Batalla del Guadalete' using Clips as a
programming language.
"""

import os

import clips

from resistencia import configure, filenames, logger
from resistencia import log_filename
log = logger.getlog('libguadalete', log_filename)

class LibGuadalete:
    """
    Main class that manages the environment and the execution of the game.
    TODO - Complete this documentation after the class is written
    """
    def __init__(self, teams, number_turns=120, piece_max_value=6):
        self.team_a = teams['team_a']
        self.team_b = teams['team_b']

        self.number_turns = number_turns
        self.piece_max_value = piece_max_value

        config_file_path = configure.__file_path__
        if not os.path.exists(config_file_path):
            log.debug('Starting configuration file on ' + config_file_path)
            configure.generate_configuration_file()

        log.debug('Created object of LibGuadalete')
