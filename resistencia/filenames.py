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

from os import path
import datetime
import types

def extract_simple_name_es (team):
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
    
    i_1 = team[0].find("/reglas")
    j_1 = team[0].find(".clp")
    i_2 = team[1].find("/equipo")
    j_2 = team[1].find(".clp")
    
    return (team[0])[i_1+7:j_1] + (team[1])[i_2+7:j_2]

def extract_names_from_file (filename):
    """
    Given the name of a game's log, extract names of the players
    """
    _file = path.split(filename)
    file_name = _file[1]

    name_a_i = 25
    name_a_j = file_name.find('-vs-')
    name_b_i = name_a_j + 4
    name_b_j = file_name.find('.txt')

    return (file_name[name_a_i:name_a_j], file_name[name_b_i:name_b_j])

def generate_filename_keys (filetype, teams=None):
    """
    Generate the name of a log file
    """
    if filetype == 'game':
        if not (type(teams) == types.TupleType) or not (len(teams) == 2):
            str_error = 'If you want to generate a filename for a game '
            str_error += 'an extra argument is needed'
            raise ValueError(str_error)

    _time = datetime.datetime.now()

    iso_date = _time.isoformat()
    iso_date = iso_date.replace('T', '_')
    iso_date = iso_date[:iso_date.find('.')]

    tail = ''
    extension = '.txt'

    if filetype == 'game':
        name_team_a = teams[0]
        name_team_b = teams[1]
        tail = '_' + name_team_a + '-vs-' + name_team_b
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

    _time = datetime.datetime.now()

    iso_date = _time.isoformat()
    iso_date = iso_date.replace('T', '_')
    iso_date = iso_date[:iso_date.find('.')]

    tail = ''
    extension = '.txt'

    if filetype == 'game':
        name_team_a = extract_name_expert_system(teams[0])
        name_team_b = extract_name_expert_system(teams[1])
        tail = '_' + name_team_a + '-vs-' + name_team_b
    if filetype == 'stats':
        tail = '_' + extract_name_expert_system(teams)
        extension = '.csv'

    filename = filetype + '_' + iso_date + tail + extension

    return filename
