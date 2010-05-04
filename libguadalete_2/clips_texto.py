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

def _clips_rule_informacion(module):
    # TODO - probably abstract the filename    
    rule_name = 'informacion'
    rule_prec = '(ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x) ' \
                '(pos-y ?y) (descubierta ?d))' \
                '(tiempo ?t)' \
                '(not (impresa ?e ?n ?t ?p))'
    rule_body = '(assert (impresa ?e ?n ?t ?p))' \
                '(open "temporal.txt" fich "a")' \
                '(a-fichero-jugador ?e ?n ?p ?x ?y ?d)' \
                '(close fich)'
                
    module.BuildRule(rule_name, rule_prec, rule_body)

 
def _clips_rule_inicial(module):
    # TODO - probably abstract the filename
    rule_name = 'inicial'
    rule_prec = '(declare (salience 100))' \
                '(tiempo ?t)' \
                '(not (iniciado ?t))' \
                '(dimension ?dim)'
    rule_body = '(open "temporal.txt" fich "a")' \
                '(a-fichero-tiempo ?t)' \
                '(close fich)' \
                '(assert (iniciado ?t))' \
                '(assert (fila (+ 1 ?dim)))' \
                '(assert (columna (+ 1 ?dim)))'
    
    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_vacia(module):
    # TODO - printout
    rule_name = 'vacia'
    rule_prec = '(declare (salience 10))' \
                '?c <- (columna ?x)' \
                '(fila ?y)' \
                '(dimension ?dim)' \
                '(test (not (> ?x ?dim)))' \
                '(not (ficha-r (pos-x ?x) (pos-y ?y)))'
    rule_body = '(retract ?c)' \
                '(assert (columna (+ ?x 1)))' \
                '(printout t "    ")'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_no_vacia(module):
    # TODO - printout
    rule_name = 'noVacia'
    rule_prec = '(declare (salience 10))' \
                '?c <- (columna ?x)' \
                '(fila ?y)' \
                '(dimension ?dim)' \
                '(test (not (> ?x ?dim)))' \
                '(ficha-r (equipo ?e) (pos-x ?x) (pos-y ?y) (puntos ?v) ' \
                '(descubierta ?d))'
    rule_body = '(retract ?c)' \
                '(assert (columna (+ ?x 1)))' \
                '(printout t " " ?e ?v (valor ?d)))'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_siguiente_fila(module):
    # TODO - printout
    rule_name = 'siguienteFila'
    rule_prec = '(declare (salience 20))' \
                '(dimension ?dim)' \
                '?c <- (columna ?x)' \
                '(test (> ?x ?dim))' \
                '?f <- (fila ?y)' \
                '(test (not (<= ?y 1)))'
    rule_body = '(retract ?c ?f)' \
                '(assert (fila (- ?y 1)))' \
                '(assert (columna 1))' \
                '(printout t crlf (- ?y 1) "|")'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_final_fila(module):
    # TODO - printout
    rule_name = 'finalFila'
    rule_prec = '(declare (salience 20))' \
                '(dimension ?dim)' \
                '?c <- (columna ?x)' \
                '(test (> ?x ?dim))' \
                '?f <- (fila ?y)' \
                '(test (= 1 ?y))'
    rule_body = '(retract ?c ?f)' \
                '(printout t crlf "----------------------------------" crlf ' \
                '"x:  1   2   3   4   5   6   7   8" crlf)'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_fin1(module):
    # TODO - printout
    rule_name = 'fin1'
    rule_prec = '(declare (salience -100))' \
                '(tiempo ?t&0)'
    rule_body = '(printout t "Fin del tiempo" crlf)' \
                '(rename "temporal.txt" "resultado.txt")'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_fin_sin_rey1(module):
    # TODO - printout
    rule_name = 'fin-sin-rey1'
    rule_prec = '(declare (salience -100))' \
                '?c <- (tiempo ?t&~0)' \
                '(not (ficha-r (equipo "A") (puntos 1)))'
    rule_body = '(printout t "Rey del equipo A muerto" crlf)' \
                '(assert (rey-A-muerto))' \
                '(rename "temporal.txt" "resultado.txt")'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_fin_sin_rey2(module):
    # TODO - printout
    rule_name = 'fin-sin-rey2'
    rule_prec = '(declare (salience -100))' \
                '?c <- (tiempo ?t&~0)' \
                '(not (ficha-r (equipo "B") (puntos 1)))'
    rule_body = '(printout t "Rey del equipo B muerto" crlf)' \
                '(assert (rey-B-muerto))' \
                '(rename "temporal.txt" "resultado.txt")'

    module.BuildRule(rule_name, rule_prec, rule_body)


class ClipsSubModuleTexto(clips_submodule.ClipsSubModule):

    def _define_submodule(self):
        submod_name = 'INFORMAR'
        submod_body = '(import MAIN deftemplate initial-fact ficha-r ' \
                      'dimension tiempo tiempo-inicial)' \
                      '(import MAIN deffunction ?ALL)'

        self.module = clips.BuildModule(submod_name, submod_body)

    def __init__(self):
        super(ClipsSubModuleTexto, self).__init__()
        self.rules = {'informacion': _clips_rule_informacion,
                      'inicial': _clips_rule_inicial,
                      'vacia': _clips_rule_vacia,
                      'noVacia': _clips_rule_no_vacia,
                      'siguienteFila': _clips_rule_siguiente_fila,
                      'finalFila': _clips_rule_final_fila,
                      'fin1': _clips_rule_fin1,
                      'fin-sin-rey1': _clips_rule_fin_sin_rey1,
                      'fin-sin-rey2': _clips_rule_fin_sin_rey2}
