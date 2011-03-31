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

rules = {'movement': ('movimiento',
                      '(declare (salience 90))' \
                          '(tiempo ?t)' \
                          '?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))' \
                          '?h2 <- (ficha-r (equipo ?e) (num ?n) (puntos ?p) ' \
                          '(pos-x ?x) (pos-y ?y) (descubierta ?d))' \
                          '(dimension ?dim)' \
                          '(tiempo-inicial ?ti)' \
                          '(test (= 0 (str-compare (turno ?ti ?t) ?e)))' \
                          '(test (mov-valido ?dim ?m ?x ?y))' \
                          '(not (ficha-r (pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) '\
                          '(pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2))))' \
                          '(not (movido ?e ?t))',
                      '(retract ?h1 ?h2)' \
                          '(printout t "Movimiento de "?e", "?n"(puntos "?p") ' \
                          ':mov "?m crlf)' \
                          '(assert (movido ?e ?t))' \
                          '(assert (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ' \
                          '(+ ?x (mov-x ?m))) (pos-y (+ ?y (mov-y ?m))) ' \
                          '(descubierta ?d)))'),
         'attack-1': ('ataque-1',
                      '(declare (salience 90))' \
                          '(tiempo ?t)' \
                          '?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))' \
                          '?h2 <- (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x)' \
                          '(pos-y ?y))' \
                          '(dimension ?dim)' \
                          '(tiempo-inicial ?ti)' \
                          '(test (= 0 (str-compare (turno ?ti ?t) ?e)))' \
                          '(test (mov-valido ?dim ?m ?x ?y))' \
                          '?h3 <- (ficha-r (equipo ?e2&~?e) (puntos ?p2&:(> ?p ?p2)) ' \
                          '(pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) (pos-y ' \
                          '?y2&:(= (+ ?y (mov-y ?m)) ?y2)))' \
                          '(not (movido ?e ?t))',
                      '(retract ?h1 ?h2 ?h3)' \
                          '(printout t "Ataque con victoria de "?n"(puntos "?p") ' \
                          ': mov "?m crlf)' \
                          '(assert (movido ?e ?t))' \
                          '(assert (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ' \
                          '(+ ?x (mov-x ?m)))(pos-y (+ ?y (mov-y ?m)))(descubierta 1)))'),
         'attack-2': ('ataque-2',
                      '(declare (salience 90))' \
                          '(tiempo ?t)' \
                          '?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))' \
                          '?h2 <- (ficha-r (equipo ?e) (num ?n) (puntos ?p) ' \
                          '(pos-x ?x) (pos-y ?y))' \
                          '(dimension ?dim)' \
                          '(tiempo-inicial ?ti)' \
                          '(test (= 0 (str-compare (turno ?ti ?t) ?e)))' \
                          '(test (mov-valido ?dim ?m ?x ?y))' \
                          '?h3 <- (ficha-r (equipo ?e2&~?e) (puntos ?p) (pos-x ?x2&:' \
                          '(= (+ ?x (mov-x ?m)) ?x2)) (pos-y ?y2&:(= (+ ?y ' \
                          '(mov-y ?m)) ?y2)))' \
                          '(not (movido ?e ?t))',
                      '(retract ?h1 ?h2 ?h3)' \
                          '(printout t "Ataque con empate de "?n"(puntos "?p") : ' \
                          'mov "?m crlf)' \
                          '(assert (movido ?e ?t))'),
         'attack-3': ('ataque-3',
                      '(declare (salience 90))' \
                          '(tiempo ?t)' \
                          '?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))' \
                          '?h2 <- (ficha-r (equipo ?e) (num ?n) (puntos ?p)' \
                          '(pos-x ?x) (pos-y ?y))' \
                          '(dimension ?dim)' \
                          '(tiempo-inicial ?ti)' \
                          '(test (= 0 (str-compare (turno ?ti ?t) ?e)))' \
                          '(test (mov-valido ?dim ?m ?x ?y))' \
                          '?h3 <- (ficha-r (equipo ?e2&~?e) (num ?n2) (puntos ?p2&:' \
                          '(< ?p ?p2)) (pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) ' \
                          '(pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2)))' \
                          '(not (movido ?e ?t))',
                      '(retract ?h1 ?h2 ?h3)' \
                          '(printout t "Ataque con derrota de "?n"' \
                          '(puntos "?p") : mov "?m crlf)' \
                          '(assert (movido ?e ?t))' \
                          '(assert (ficha-r (equipo ?e2) (num ?n2) (puntos ?p2) ' \
                          '(pos-x ?x2) (pos-y ?y2) (descubierta 1)))'),
         'clean': ('limpia',
                   '(declare (salience 0))' \
                       '?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))',
                   '(retract ?h1)'),
}


module_name = 'MOVER'


module_body = '(import MAIN deftemplate initial-fact ficha-r ' \
    'dimension tiempo mueve turno tiempo-inicial)' \
    '(import MAIN deffunction ?ALL)'
