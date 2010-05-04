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

import clips_submodule

def _clips_rule_movimiento(module):
    # TODO - printout'
    rule_name = 'movimiento'
    rule_prec = '(declare (salience 90))' \
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
                '(not (movido ?e ?t))'
    rule_body = '(retract ?h1 ?h2)' \
                '(printout t "Movimiento de "?e", "?n"(puntos "?p") ' \
                ':mov "?m crlf)' \
                '(assert (movido ?e ?t))' \
                '(assert (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ' \
                '(+ ?x (mov-x ?m))) (pos-y (+ ?y (mov-y ?m))) ' \
                '(descubierta ?d)))'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_ataque_1(module):
    # TODO - printout
    rule_name = 'ataque-1'
    rule_prec = '(declare (salience 90))' \
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
                '(not (movido ?e ?t))'
    rule_body = '(retract ?h1 ?h2 ?h3)' \
                '(printout t "Ataque con victoria de "?n"(puntos "?p") ' \
                ': mov "?m crlf)' \
                '(assert (movido ?e ?t))' \
                '(assert (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ' \
                '(+ ?x (mov-x ?m)))(pos-y (+ ?y (mov-y ?m)))(descubierta 1)))' \

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_ataque_2(module):
    # TODO - printout
    rule_name = 'ataque-2'
    rule_prec = '(declare (salience 90))' \
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
                '(not (movido ?e ?t))'
    rule_body = '(retract ?h1 ?h2 ?h3)' \
                '(printout t "Ataque con empate de "?n"(puntos "?p") : ' \
                'mov "?m crlf)' \
                '(assert (movido ?e ?t))' \

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_ataque_3(module):
    # TODO - printout
    rule_name = 'ataque-3' 
    rule_prec = '(declare (salience 90))' \
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
                '(not (movido ?e ?t))'
    rule_body = '(retract ?h1 ?h2 ?h3)' \
                '(printout t "Ataque con derrota de "?n"' \
                '(puntos "?p") : mov "?m crlf)' \
                '(assert (movido ?e ?t))' \
                '(assert (ficha-r (equipo ?e2) (num ?n2) (puntos ?p2) ' \
                '(pos-x ?x2) (pos-y ?y2) (descubierta 1)))'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_limpia(module):
    rule_name = 'limpia'
    rule_prec = '(declare (salience 0))' \
                '?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))'
    rule_body = '(retract ?h1)'

    module.BuildRule(rule_name, rule_prec, rule_body)
    

class ClipsSubModuleMover(clips_submodule.ClipsSubModule):
    
    def _define_submodule(self):
        submod_name = 'MOVER'
        submod_body = '(import MAIN deftemplate initial-fact ficha-r ' \
                      'dimension tiempo mueve turno tiempo-inicial)' \
                      '(import MAIN deffunction ?ALL)'
        print submod_name
        print submod_body

        self.module = clips.BuildModule(submod_name, submod_body)
        
    def __init__(self):
        super(ClipsSubModuleMover, self).__init__()
        self.rules = {'movimiento': _clips_rule_movimiento,
                      'ataque-1': _clips_rule_ataque_1,
                      'ataque-2': _clips_rule_ataque_2,
                      'ataque-3': _clips_rule_ataque_3,
                      'limpia': _clips_rule_limpia}
