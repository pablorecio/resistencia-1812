# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# This file is part of Resistencia Cadiz 1812.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Copyright (C) 2009, Pablo Recio Quijano
#----------------------------------------------------------------------

import clips
import os
import datetime
import random

import sys
sys.path.append("./libguadalete")
import funciones
import f1
import mover
import texto
import traducirF
import traducirM
import fA
import fB

import mirroring

import configure

class LibGuadalete(object):
    """
    This class provides an abstraction layer that allows run a simulation of 'La batalla del Guadalete',
    generating a file that can be parsered easily.
    @todo It's necessary to ad a lot of funcionality on this module, like human vs computer. 
    """
    def __init__(self, teamA, teamB, teams_path = '../teams'):
        """
        Class <code>LibGuadalete</code> constructor. Just assign variables.
        @param self Object that will be initialized
        @param teamA Tuple with paths to the rule file and formation file for the A team.
        @param teamB Tuple with paths to the rule file and formation file for the B team.
        @param teams_path Path to the directory that teams are stored by default
        """
        #print teamA
        #print teamB
        self.teamA = teamA
        self.teamB = teamB
        self.teams_path = teams_path
        self.max_value = 6

    def __startGame(self):
        clips.Clear()
        
        clips.EngineConfig.Strategy = clips.RANDOM_STRATEGY

        random.seed()
        clips.Eval("(seed " + str(random.randint(0,9999)) + ")") 

        funciones.LoadFunctions(clips)
        f1.LoadFunctions(clips)
        mover.LoadFunctions(clips)
        texto.LoadFunctions(clips)
        traducirF.LoadFunctions(clips)
        traducirM.LoadFunctions(clips)

        #print self.teams_path + "/equipo" + self.teamA + ".clp"
        temp_team = mirroring.mirroring_team(self.teamB[1])
        clips.Load(self.teamA[1])
        clips.Load(temp_team)
        os.remove(temp_team)

        fA.LoadFunctions(clips)
        clips.Load(self.teamA[0])
        temp_rules = mirroring.mirroring_rules(self.teamB[0])
        fB.LoadFunctions(clips)
        clips.Load(temp_rules)
        os.remove(temp_rules)

        clips.Reset()

        clips.PrintFacts()
        clips.PrintModules()

        clips.Run()
        t = clips.StdoutStream.Read()

        print t

    def __generateFileName(self):
        t = datetime.datetime.now()

        if (t.month < 10):
            month = "0" + str(t.month)
        else:
            month = str(t.month)
            
        if (t.day < 10):
            day = "0" + str(t.day)
        else:
            day = str(t.day)

        if (t.hour < 10):
            hour = "0" + str(t.hour)
        else:
            hour = str(t.hour)
    
        if (t.minute < 10):
            min = "0" + str(t.minute)
        else:
            min = str(t.minute)

        if (t.second < 10):
            sec = "0" + str(t.second)
        else:
            sec = str(t.second)

        i_a = self.teamA[1].find("/equipo")
        i_b = self.teamB[1].find("/equipo")
        j_a = self.teamA[1].find(".clp")
        j_b = self.teamB[1].find(".clp")
        
        teamA = (self.teamA[1])[i_a+7:j_a]
        teamB = (self.teamB[1])[i_b+7:j_b]
    
        des = str(t.year) + "-" + month + "-" + day + "_"
        des += hour + ":" + min + ":" + sec + "_" + teamA + "-vs-" + teamB
        #des += hour + ":" + min + ":" + sec
        des += ".txt"

        base_path = configure.load_configuration()['games_path']

        return base_path + '/' + des

    def __renameOutputFile(self,des):
        src = "resultado.txt"
        f = open(src,"a")
        f.write("fin\n")
        print "src: " + src
        print "des: " + des
        os.rename(src, des)

    def run_game(self):
        """
        Method that make the expert systems play the game, and generate the output file.
        @return String with the path to the output file
        """
        self.__startGame()
        des = self.__generateFileName()
        self.__renameOutputFile(des)

        return des
