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

        return des

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

    #temporal
    def __mirror_team(self, team):
        src = "tempTeam.clp"
        f_team = open(team,"r")
        f_temp = open(src, "w")

        for l in f_team:
            new_line = l
            if new_line[0] != ';':
                new_line = new_line.replace("A","B")
                new_line = new_line.replace("(pos-y 1)", "(pos-y 8)")
                new_line = new_line.replace("(pos-y 2)", "(pos-y 7)")
            f_temp.write(new_line)

        return src

    #Parte de parseo del fichero, temporal, aun tengo que ver si lo
    #dejo en esta clase

    def __fillMatrix(self,x = 8, y = 8, value = 0):
        m = []
        for i in range(x):
            f = []
            for j in range(y):
                f.append(value)
            m.append(f)
                
        return m  

    def parseFile(self,srcFile):
        """
        This function allows to parse an output file generated on a simulation, and generate
        a data structure more computer readable.
        @param srcFile File with a game played.
        @return A list with the boards for every single turn on a game.
        @todo See if it's the right place for this function
        """
        f = open(srcFile)

        line = "0" #line value not null for the loop
        
        values = {}
        entireGame = []
        counter = 0
        
        while line != "":
            line = f.readline()
            if (line == "tiempo\n" or line == "fin\n"): #If we are in a new turn
                try: board
                except NameError:
                    board = self.__fillMatrix()
                else:
                    entireGame.append(board) #include the board on the game
                    counter += 1
                    del board
                    board = self.__fillMatrix() #restart the board from 0
            else:
                if (line != "\n" and len(line) > 5):
                    pos_e = line.find("e")
                    pos_id = line.find("n")
                    pos_val = line.find("p")
                    pos_x = line.find("x")
                    pos_y = line.find("y")
                    pos_d = line.find("d")
                    
                    e = line[pos_e+2:pos_id-1]
                    id = line[pos_id+2:pos_val-1]
                    val = line[pos_val+2:pos_x-1]
                    x = line[pos_x+2:pos_y-1]
                    y = line[pos_y+2:pos_d-1]
                    d = line[pos_d+2:]
                
                    values[id] = val

                    if e == 'A':
                        board[int(y) - 1][int(x) - 1] = int(val) + (int(d)*self.max_value)
                    else:
                        board[int(y) - 1][int(x) - 1] = int(val) - 2*int(val) - (int(d)*self.max_value)
                
        f.close()

        return entireGame
