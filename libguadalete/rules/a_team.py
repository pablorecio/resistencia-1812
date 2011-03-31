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
# Copyright (C) 2011, Pablo Recio Quijano, <pablo.recioquijano@gmail.com>     #
###############################################################################

rules = {
    'basic1': ('basica1',
               '(declare (salience 1))' \
                   '(tiempo ?t)' \
                   '(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y))' \
                   '(dimension ?dim&:(< ?x (/ ?dim 2)))' \
                   '(not (ficha (equipo "A") (pos-x ?x2&:(= ?x2 ' \
                   '(+ ?x 1))) (pos-y ?y)))',
               '(printout t "EQUIPO-A mueve a" ?n " hacia 1 en t " ?t crlf)' \
                   '(assert (mueve (num ?n) (mov 1) (tiempo ?t)))'),
    'basic2': ('basica2',
               '(declare (salience 1))' \
                   '(tiempo ?t)' \
                   '(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y))' \
                   '(dimension ?dim&:(> ?x (/ ?dim 2)))' \
                   '(not (ficha (equipo "A") (pos-x ?x2&:(= ?x2 ' \
                   '(- ?x 1))) (pos-y ?y)))',
               '(printout t "EQUIPO-A mueve a" ?n " hacia 2 en t " ?t crlf)' \
                   '(assert (mueve (num ?n) (mov 2) (tiempo ?t)))'),
    'basic3': ('basica3',
               '(declare (salience 1))' \
                   '(tiempo ?t)' \
                   '(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y))' \
                   '(dimension ?dim&:(< ?y (/ ?dim 2)))' \
                   '(not (ficha (equipo "A") (pos-x ?x) (pos-y ?y2&:(= ?y2 ' \
                   '(+ ?y 1)))))',
               '(printout t "EQUIPO-A mueve a" ?n " hacia 3 en t " ?t crlf)' \
                   '(assert (mueve (num ?n) (mov 3) (tiempo ?t)))'),
    'basic4': ('basica4',
               '(declare (salience 1))' \
                   '(tiempo ?t)' \
                   '(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y))' \
                   '(dimension ?dim&:(> ?y (/ ?dim 2)))' \
                   '(not (ficha (equipo "A") (pos-x ?x) (pos-y ?y2&:(= ' \
                   '?y2 (- ?y 1)))))',
               '(printout t "EQUIPO-A mueve a" ?n " hacia 4 en t " ?t crlf)' \
                   '(assert (mueve (num ?n) (mov 4) (tiempo ?t)))'),
    'finish': ('termina',
               '(declare (salience 100))' \
                   '(tiempo ?t)' \
                   '(dimension ?dim)' \
                   '(mueve (num ?n) (mov ?m) (tiempo ?t))' \
                   '(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y))' \
                   '(test (mov-valido ?dim ?m ?x ?y))' \
                   '(not (ficha (equipo "A")  (pos-x ?x2&:(= (+ ?x ' \
                   '(mov-x ?m)) ?x2)) (pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2))))',
               '(pop-focus)'),
}


module_name = 'EQUIPO-A'


module_body = '(import MAIN deftemplate initial-fact ficha ' \
    'dimension tiempo mueve tiempo-inicial)' \
    '(import MAIN deffunction ?ALL)'
