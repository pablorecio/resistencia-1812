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
# Copyright(C) 2009,2010 Pablo Recio Quijano <pablo.recioquijano@alum.uca.es> #
###############################################################################

"""
This module intialize the Clips environment for the 1 player mode
"""

import os
import random

import clips

import guadaboard.real_interaction as r_intact

from libguadalete import funciones, f1, mover, texto
from libguadalete import traducirF, traducirM, fA, fB, mirroring, interaccion

from resistencia import configure, filenames, xdg
from resistencia.nls import gettext as _


def _generate_file_name(team_a, team_b):
    """This function generate a proper filename for the game log

    Return a string like 'game_YYYY-MM-DD_hh:mm:ss_team_a-vs-team_b.txt'
    """
    des = filenames.generate_filename_keys('game',
                                           (team_a, team_b))

    base_path = configure.load_configuration()['games_path']

    return base_path + '/' + des

def _rename_output_file(des):
    """
    Simple function that rename the output file named 'resultado.txt'
    to the proper filename with the date, names and so on.
    """
    src = "resultado.txt"
    _file = open(src,"a")
    _file.write("fin\n")
    print "src: " + src
    print "des: " + des
    os.rename(src, des)

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class FileError(Error):
    """Exception raised for errors parsing files

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg

def init_human_game(player_formation, computer_team, player_as,
                    number_turns, dont_save=False):
    """
    Intialize the clips environment
    """
    player_num = 0
    team_a = None
    team_b = None
    name_team_a = ''
    name_team_b = ''
    
    team_a_piece = xdg.get_data_path('images/piece-orange.png')
    team_b_piece = xdg.get_data_path('images/piece-violete.png')
    default_piece = xdg.get_data_path('images/piece-default.png')
    
    if player_as == 'A':
        player_num = 1
        team_a = player_formation
        team_b = computer_team
        name_team_a = filenames.extract_simple_name_es((None, team_a))
        name_team_b = filenames.extract_name_expert_system(team_b)
    else:
        player_num = -1
        team_b = player_formation
        team_a = computer_team
        name_team_b = filenames.extract_simple_name_es((None, team_b))
        name_team_a = filenames.extract_name_expert_system(team_a)

    print team_a
    print team_b
    
    aux_team_a = (name_team_a, team_a_piece)
    aux_team_b = (name_team_b, team_b_piece)

    clips.Eval('(clear)')
        
    clips.EngineConfig.Strategy = clips.RANDOM_STRATEGY

    random.seed()
    clips.Eval("(seed " + str(random.randint(0, 9999)) + ")") 

    funciones.LoadFunctions(clips)
    f1.init_world(clips, number_turns)
    f1.LoadFunctions(clips)
    mover.LoadFunctions(clips)
    texto.LoadFunctions(clips)
    traducirF.LoadFunctions(clips)
    traducirM.LoadFunctions(clips)

    if player_num == 1:
        int_team = mirroring.interactive_formation(team_a)
        temp_team = mirroring.mirroring_team(team_b[1])

        try:
            clips.Load(int_team)
        except clips.ClipsError:
            os.remove(int_team)
            raise FileError(_('Error parsing the file ') +  team_a)

        try:
            clips.Load(temp_team)
        except clips.ClipsError:
            os.remove(temp_team)
            raise FileError(_('Error parsing the file ') +  team_b[1])

        os.remove(int_team)
        os.remove(temp_team)
        
        fB.LoadFunctions(clips)
        temp_rules = mirroring.mirroring_rules(team_b[0])
        try:
            clips.Load(temp_rules)
        except clips.ClipsError:
            os.remove(temp_rules)
            raise FileError(_('Error parsing the file ') +  team_b[0])
        os.remove(temp_rules)
    else:
        try:
            clips.Load(team_a[1])
        except clips.ClipsError:
            raise FileError(_('Error parsing the file ') +  team_a[1])
        
        int_team = mirroring.interactive_formation(team_b)
        temp_team = mirroring.mirroring_team(int_team)

        try:
            clips.Load(temp_team)
        except clips.ClipsError:
            os.remove(temp_team)
            raise FileError(_('Error parsing the file ') +  team_a[1])
        os.remove(temp_team)

        fA.LoadFunctions(clips)
        try:
            clips.Load(team_a[0])
        except clips.ClipsError:
            raise FileError(_('Error parsing the file ') +  team_a[0])
 
    interaccion.LoadFunctions(clips, player_as)
    
    interaccion.interaction_object = r_intact.HumanInteraction(aux_team_a,
                                                               aux_team_b,
                                                               default_piece,
                                                               player_num,
                                                               number_turns)
    
    clips.Reset() #restart the environment

    clips.Run() #start the simulation
    interaccion.interaction_object.finish()
    _stream = clips.StdoutStream.Read() #print the output

    print _stream
    print interaccion.interaction_object.define_winner()

    if not dont_save:
        _rename_output_file(_generate_file_name(name_team_a, name_team_b))
    os.remove('resultado.txt')
