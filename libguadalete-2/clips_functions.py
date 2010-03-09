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
This file contains the definition of functions used on the clips environment
"""

import clips

from resistencia import logger
from resistencia import log_filename
log = logger.getlog('libguadalete.clips_functions', log_filename)

def _file_new_turn (filename, turn):
    f = open(filename, 'a')
    f.write('tiempo ' + str(turn))
    log.debug('Init turn number ' + str(turn) + ' on "' + filename + '"')
    f.close()

def _file_new_piece (filename, team, nid, value, x, y, covered):
    line = 'e:' + team + ' n:' + nid + ' p:' + value \
           + ' x:' + x + ' y:' + y + ' d:' + covered + "\n"
    f = open(filename, 'a')
    f.write(line)
    log.debug('Writed line "' + line + '" on "' filename '"')
    f.close()

def _clips_distancia():
    # First function name
    fun_name = 'distancia'
    # Parameters for the function
    fun_param = '?x1 ?y1 ?x2 ?y2'
    # Function body
    fun_body = '(sqrt (+ (* (- ?x1 ?x2) (- ?x1 ?x2))' \
               '(* (- ?y1 ?y2) (- ?y1 ?y2))))'
    clips.BuildFunction(fun_name, fun_param, fun_body)

def _clips_dentro():
    # Function name
    fun_name = 'dentro'
    # Function parameters
    fun_param  = '?x1 ?y1 ?x2 ?y2 ?x ?y'
    # Function body
    fun_body  = '(and (or (<= ?x1 ?x ?x2) (>= ?x1 ?x ?x2))' \
                '(or (<= ?y1 ?y ?y2) (>= ?y1 ?y ?y2)))'
    # Building the function
    clips.BuildFunction(fun_name, fun_param, fun_body)

def _clips_minimo():
    fun_name = 'minimo'
    fun_param = '?n1 ?n2'
    fun_body = '(if (< ?n1 ?n2) then '\
               '?n1 '\
               'else '\
               '?n2'
    clips.BuildFunction(fun_name, fun_param, fun_body)

#clips.RegisterPythonFunction(clips_raw_input, "raw-input")
#(bind ?user-name (python-call raw-input "Your Name? "))

_functions = [_clips_distancia, _clips_dentro, _clips_minimo]

def init_module():
    clips.RegisterPythonFunction(_file_new_turn, 'a-fichero-tiempo')
    clips.RegisterPythonFunction(_file_new_piece, 'a-fichero-jugador')

    for f in _functions:
        f()
