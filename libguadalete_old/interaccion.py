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

import clips
import time

from guadaboard import real_interaction

interaction_object = real_interaction.HumanInteraction

def clips_piece_input():
    #get the value someway
    print 'clips_piece_input()'
    #interaction_object.update_games()
    val = interaction_object.get_identifier_last_move()
    print 'tras interaction_object.get_identifier_last_move()'
    print val
    return clips.Integer(val)

def clips_move_input():
    #get the value someway
    print 'clips_move_input()'
    val = interaction_object.get_movement_last_move()
    print val
    return clips.Integer(val)

clips.RegisterPythonFunction(clips_piece_input, "piece-input")
clips.RegisterPythonFunction(clips_move_input, "move-input")

def LoadFunctions(clips, team):
    # Generates the CLIPS module
    mod_name = "EQUIPO-" + team
    # Module body
    mod_body  = "(import MAIN deftemplate initial-fact ficha dimension "\
                "tiempo mueve tiempo-inicial)"
    mod_body += "(import MAIN deffunction ?ALL)"
    mod_equipo = clips.BuildModule(mod_name, mod_body)

    # Function that reads the movement 
    fun_name = 'read-mov'
    fun_para = '?n ?t'
    fun_body = '(bind ?mov (python-call move-input))'
    fun_body  += '(printout t "EQUIPO-B mueve a" ?n " hacia " ?mov " en t " ?t crlf)'
    fun_body += '(assert (mueve (num ?n) (mov ?mov) (tiempo ?t)))'

    fun_lectura_mov = mod_equipo.BuildFunction(fun_name, fun_para, fun_body)

    # rule with max salience that will be trigged on every turn
    rule_name = 'lectura' + team

    rule_prec = '(declare (salience 100))'
    rule_prec += '(tiempo ?t)'

    rule_body  = '(bind ?n (python-call piece-input))'
    rule_body += '(read-mov ?n ?t)'

    lectura = mod_equipo.BuildRule(rule_name, rule_prec, rule_body)
    
    # Rule name
    rule_name = 'termina'
    # Rule precontents
    rule_prec  = '(declare (salience 100))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '(dimension ?dim)'
    rule_prec += '(mueve (num ?n) (mov ?m) (tiempo ?t))'
    rule_prec += '(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y))'
    rule_prec += '(test (mov-valido ?dim ?m ?x ?y))'
    rule_prec += '(not (ficha (equipo "A")  (pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) (pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2))))'
    # =>
    # Rule body
    rule_body  = '(pop-focus)'
    # Building the rule
    termina = mod_equipo.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------
