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
    'information': ('informacion',
                    '(ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x) ' \
                        '(pos-y ?y) (descubierta ?d))' \
                        '(tiempo ?t)' \
                        '(not (impresa ?e ?n ?t ?p))',
                    '(assert (impresa ?e ?n ?t ?p))' \
                        '(open "temporal.txt" fich "a")' \
                        '(a-fichero-jugador ?e ?n ?p ?x ?y ?d)' \
                        '(close fich)'),
    'initial': ('inicial',
                '(declare (salience 100))' \
                    '(tiempo ?t)' \
                    '(not (iniciado ?t))' \
                    '(dimension ?dim)',
                '(open "temporal.txt" fich "a")' \
                    '(a-fichero-tiempo ?t)' \
                    '(close fich)' \
                    '(assert (iniciado ?t))' \
                    '(assert (fila (+ 1 ?dim)))' \
                    '(assert (columna (+ 1 ?dim)))'),
    'empty': ('vacia',
              '(declare (salience 10))' \
                  '?c <- (columna ?x)' \
                  '(fila ?y)' \
                  '(dimension ?dim)' \
                  '(test (not (> ?x ?dim)))' \
                  '(not (ficha-r (pos-x ?x) (pos-y ?y)))',
              '(retract ?c)' \
                  '(assert (columna (+ ?x 1)))' \
                  '(printout t "    ")'),
    'notempty': ('noVacia',
                 '(declare (salience 10))' \
                     '?c <- (columna ?x)' \
                     '(fila ?y)' \
                     '(dimension ?dim)' \
                     '(test (not (> ?x ?dim)))' \
                     '(ficha-r (equipo ?e) (pos-x ?x) (pos-y ?y) (puntos ?v) ' \
                     '(descubierta ?d))',
                 '(retract ?c)' \
                     '(assert (columna (+ ?x 1)))' \
                     '(printout t " " ?e ?v (valor ?d)))'),
    'nextrow': ('siguienteFila',
                '(declare (salience 20))' \
                    '(dimension ?dim)' \
                    '?c <- (columna ?x)' \
                    '(test (> ?x ?dim))' \
                    '?f <- (fila ?y)' \
                    '(test (not (<= ?y 1)))',
                '(retract ?c ?f)' \
                    '(assert (fila (- ?y 1)))' \
                    '(assert (columna 1))' \
                    '(printout t crlf (- ?y 1) "|")'),
    'finalrow': ('finalFila',
                 '(declare (salience 20))' \
                     '(dimension ?dim)' \
                     '?c <- (columna ?x)' \
                     '(test (> ?x ?dim))' \
                     '?f <- (fila ?y)' \
                     '(test (= 1 ?y))',
                 '(retract ?c ?f)' \
                     '(printout t crlf "----------------------------------" crlf ' \
                     '"x:  1   2   3   4   5   6   7   8" crlf)'),
    'end': ('fin1',
            '(declare (salience -100))' \
                '(tiempo ?t&0)',
            '(printout t "Fin del tiempo" crlf)' \
                '(rename "temporal.txt" "resultado.txt")'),
    'end-w-king1': ('fin-sin-rey1',
                    '(declare (salience -100))' \
                        '?c <- (tiempo ?t&~0)' \
                        '(not (ficha-r (equipo "A") (puntos 1)))',
                    '(printout t "Rey del equipo A muerto" crlf)' \
                        '(assert (rey-A-muerto))' \
                        '(rename "temporal.txt" "resultado.txt")'),
    'end-w-king2': ('fin-sin-rey2',
                    '(declare (salience -100))' \
                        '?c <- (tiempo ?t&~0)' \
                        '(not (ficha-r (equipo "B") (puntos 1)))',
                    '(printout t "Rey del equipo B muerto" crlf)' \
                        '(assert (rey-B-muerto))' \
                        '(rename "temporal.txt" "resultado.txt")'),
}


module_name = 'INFORMAR'


module_body = '(import MAIN deftemplate initial-fact ficha-r ' \
    'dimension tiempo tiempo-inicial)' \
    '(import MAIN deffunction ?ALL)'
