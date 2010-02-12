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
This file provides some functions commonly used in all the application.
"""

import os
from os import path
import datetime
import random
import types

def extract_simple_name_expert_system (team):
    """Reciving a 2 elements tuple, extract the name of the player.

    Keywords arguments:
    team -- Tuple with the names of the rules and formation files.
    """
    if not (type(team) == types.TupleType) or not (len(team) == 2):
        str_error = 'Variable must be a pair '
        raise ValueError(str_error)

    i = team[1].find("/equipo")
    j = team[1].find(".clp")

    return (team[1])[i+7:j]

def extract_name_expert_system(team):
    """Reciving a 2 elements tuple, extract the name of the player
    using the 2 files instead of only one.

    Keywords arguments:
    team -- Tuple with the names of the rules and formation files.
    """
    if not (type(team) == types.TupleType) or not (len(team) == 2):
        str_error = 'Variable must be a pair '
        raise ValueError(str_error)
    
    i1 = team[0].find("/reglas")
    j1 = team[0].find(".clp")
    i2 = team[1].find("/equipo")
    j2 = team[1].find(".clp")
    
    return (team[0])[i1+7:j1] + (team[1])[i2+7:j2]

def extract_names_from_file (filename):
    """
    Given the name of a game's log, extract names of the players
    """
    useless, file_name = path.split(filename)

    nameA_i = 25
    nameA_j = file_name.find('-vs-')
    nameB_i = nameA_j + 4
    nameB_j = file_name.find('.txt')

    return (file_name[nameA_i:nameA_j], file_name[nameB_i:nameB_j])

def generate_filename_keys (filetype, teams=None):
    if filetype == 'game':
        if not (type(teams) == types.TupleType) or not (len(teams) == 2):
            str_error = 'If you want to generate a filename for a game '
            str_error += 'an extra argument is needed'
            raise ValueError(str_error)

    t = datetime.datetime.now()

    iso_date = t.isoformat()
    iso_date = iso_date.replace('T', '_')
    iso_date = iso_date[:iso_date.find('.')]

    tail = ''
    extension = '.txt'

    if filetype == 'game':
        name_teamA = teams[0]
        name_teamB = teams[1]
        tail = '_' + name_teamA + '-vs-' + name_teamB
    if filetype == 'stats':
        tail = '_' + extract_name_expert_system(teams)
        extension = '.csv'

    filename = filetype + '_' + iso_date + tail + extension

    return filename


def generate_filename (filetype, teams=None):
    """This function allow to generates files with proper name.

    Keyword arguments:
    filetype -- String that indicates what type of file we want. Could be
    'game', 'league', 'tournament'
    teams -- If filetype is 'game', teams must be a tuple of 2 elements,
    containing the path of the files that compose the expert system.
    """
    if filetype == 'game':
        if not (type(teams) == types.TupleType) or not (len(teams) == 2):
            str_error = 'If you want to generate a filename for a game '
            str_error += 'an extra argument is needed'
            raise ValueError(str_error)

    t = datetime.datetime.now()

    iso_date = t.isoformat()
    iso_date = iso_date.replace('T', '_')
    iso_date = iso_date[:iso_date.find('.')]

    tail = ''
    extension = '.txt'

    if filetype == 'game':
        name_teamA = extract_name_expert_system(teams[0])
        name_teamB = extract_name_expert_system(teams[1])
        tail = '_' + name_teamA + '-vs-' + name_teamB
    if filetype == 'stats':
        tail = '_' + extract_name_expert_system(teams)
        extension = '.csv'

    filename = filetype + '_' + iso_date + tail + extension

    return filename
