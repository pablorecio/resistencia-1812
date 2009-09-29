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

import parseOutput #parseOutput.py

teamA = "A"
teamB = "B"
des = ""

def startGame():
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
    
    clips.Load("teams/equipo" + teamA + ".clp")
    clips.Load("teams/equipo" + teamB + ".clp")
    
    fA.LoadFunctions(clips)
    clips.Load("teams/reglas" + teamA + ".clp")
    fB.LoadFunctions(clips)
    clips.Load("teams/reglas" + teamB + ".clp")
    
    clips.Reset()
    
    clips.PrintFacts()
    clips.PrintModules()
    
    clips.Run()

def generateFileName():
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
    
    des = str(t.year) + "-" + month + "-" + day + "_"
    des += hour + ":" + min + ":" + sec + "_" + teamA + "-vs-" + teamB
    des += ".txt"

    return des
    

def renameOutputFile(des):
    src = "resultado.txt"
    f = open(src,"a")
    f.write("fin\n")
    print "src: " + src
    print "des: " + des
    os.rename(src, des)

if __name__ == "__main__":
    startGame()

    outputFile = generateFileName()
    print outputFile
    renameOutputFile(outputFile)
    entireGame = parseOutput.parseFile(outputFile)
    for i in entireGame:
        print i
        raw_input("Pulse una tecla")
    #print entireGame[len(entireGame)-1]
    
        
