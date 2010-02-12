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

import os
import random
import sys

import clips

import real_interaction

from libguadalete import funciones, f1, mover, texto
from libguadalete import traducirF, traducirM, fA, fB, mirroring, interaccion

from resistencia import configure, filenames, xdg
from resistencia.nls import gettext as _


def _generateFileName(teamA, teamB):
    """This function generate a proper filename for the game log

    Return a string like 'game_YYYY-MM-DD_hh:mm:ss_teamA-vs-teamB.txt'
    """
    des = filenames.generate_filename_keys('game',
                                           (teamA, teamB))

    base_path = configure.load_configuration()['games_path']

    return base_path + '/' + des

def _renameOutputFile(des):
    """
    Simple function that rename the output file named 'resultado.txt'
    to the proper filename with the date, names and so on.
    """
    src = "resultado.txt"
    f = open(src,"a")
    f.write("fin\n")
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

def init_human_game(player_formation, computer_team, player_as, number_turns, dont_save=False):
    player_num = 0
    teamA = None
    teamB = None
    name_teamA = ''
    name_teamB = ''
    
    teamA_piece = xdg.get_data_path('images/piece-orange.png')
    teamB_piece = xdg.get_data_path('images/piece-violete.png')
    default_piece = xdg.get_data_path('images/piece-default.png')
    
    if player_as == 'A':
        player_num = 1
        teamA = player_formation
        teamB = computer_team
        name_teamA = filenames.extract_simple_name_expert_system((None,teamA))
        name_teamB = filenames.extract_name_expert_system(teamB)
    else:
        player_num = -1
        teamB = player_formation
        teamA = computer_team
        name_teamB = filenames.extract_simple_name_expert_system((None,teamB))
        name_teamA = filenames.extract_name_expert_system(teamA)

    print teamA
    print teamB
    
    aux_teamA = (name_teamA, teamA_piece)
    aux_teamB = (name_teamB, teamB_piece)

    clips.Eval('(clear)')
        
    clips.EngineConfig.Strategy = clips.RANDOM_STRATEGY

    random.seed()
    clips.Eval("(seed " + str(random.randint(0,9999)) + ")") 

    funciones.LoadFunctions(clips)
    f1.init_world(clips, number_turns)
    f1.LoadFunctions(clips)
    mover.LoadFunctions(clips)
    texto.LoadFunctions(clips)
    traducirF.LoadFunctions(clips)
    traducirM.LoadFunctions(clips)

    if player_num == 1:
        int_team = mirroring.interactive_formation(teamA)
        temp_team = mirroring.mirroring_team(teamB[1])

        try:
            clips.Load(int_team)
        except clips.ClipsError:
            os.remove(int_team)
            raise FileError(_('Error parsing the file ') +  teamA)

        try:
            clips.Load(temp_team)
        except clips.ClipsError:
            os.remove(temp_team)
            raise FileError(_('Error parsing the file ') +  teamB[1])

        os.remove(int_team)
        os.remove(temp_team)
        
        fB.LoadFunctions(clips)
        temp_rules = mirroring.mirroring_rules(teamB[0])
        try:
            clips.Load(temp_rules)
        except clips.ClipsError:
            os.remove(temp_rules)
            raise FileError(_('Error parsing the file ') +  teamB[0])
        os.remove(temp_rules)
    else:
        try:
            clips.Load(teamA[1])
        except clips.ClipsError:
            raise FileError(_('Error parsing the file ') +  teamA[1])
        
        int_team = mirroring.interactive_formation(teamB)
        temp_team = mirroring.mirroring_team(int_team)

        try:
            clips.Load(temp_team)
        except clips.ClipsError:
            os.remove(temp_team)
            raise FileError(_('Error parsing the file ') +  teamA[1])
        os.remove(temp_team)

        fA.LoadFunctions(clips)
        try:
            clips.Load(teamA[0])
        except clips.ClipsError:
            raise FileError(_('Error parsing the file ') +  teamA[0])
 
    interaccion.LoadFunctions(clips, player_as)
    
    interaccion.interaction_object = real_interaction.HumanInteraction(aux_teamA,
                                                                       aux_teamB,
                                                                       default_piece,
                                                                       player_num,
                                                                       number_turns)
    
    clips.Reset() #restart the environment

    clips.Run() #start the simulation
    interaccion.interaction_object.finish()
    t = clips.StdoutStream.Read() #print the output

    print t
    print interaccion.interaction_object.define_winner()

    if not dont_save:
        _renameOutputFile(_generateFileName(name_teamA, name_teamB))
    os.remove('resultado.txt')
