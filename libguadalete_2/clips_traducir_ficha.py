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

import clips_submodule

def _clips_rule_inicial_1_0(module):
    # TODO - printout
    rule_name = 'inicial1-0'
    rule_prec = '(declare (salience 100))' \
                '(tiempo ?t)'
    rule_body = '(printout t "**********************************" crlf )'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_inicial_1_1(module):
    rule_name = 'inicial1-1'
    rule_prec = '(declare (salience 100))' \
                '(tiempo ?t)' \
                '(test (= 0 (mod ?t 2)))'
    rule_body = '(assert (equipoA ?t "B"))'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_inicial_2(module):
    rule_name = 'inicial2'
    rule_prec = '(declare (salience 100))' \
                '(tiempo ?t)' \
                '(test (<> 0 (mod ?t 2)))'
    rule_body = '(assert (equipoA ?t "A"))'
    
    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_elimina_1(module):
    rule_name = 'elimina1'
    rule_prec = '(declare (salience 20))' \
                '(tiempo ?t)' \
                '?h <- (ficha (num ?n) (equipo ?e) (pos-x ?x) ' \
                '(pos-y ?y) (puntos ?v) (descubierta ?d))' \
                '(not (limpia ?t))'
    rule_body = '(retract ?h)'
    
    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_elimina_2(module):
    # TODO - printout
    rule_name = 'elimina2'
    rule_prec = '(declare (salience 20))' \
                '(tiempo ?t)'
    rule_body = '(printout t "*Limpiado" ?t  crlf)' \
                '(assert (limpia ?t))'
    
    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_directo_0A(module):
    rule_name = 'directo-0A'
    rule_prec = '(declare (salience 10))' \
                '(tiempo ?t)' \
                '(equipoA ?t "A")' \
                '(ficha-r (num ?n) (equipo "A") (pos-x ?x) ' \
                '(pos-y ?y) (puntos ?v) (descubierta 0))'
    rule_body = '(assert (ficha (num ?n) (equipo "A") (pos-x ?x) ' \
                '(pos-y ?y) (puntos ?v) (descubierta 0)))'
    
    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_directo_0B(module):
    rule_name = 'directo-0B'
    rule_prec = '(declare (salience 10))' \
                '(tiempo ?t)' \
                '(equipoA ?t "A")' \
                '(ficha-r (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) ' \
                '(puntos ?v) (descubierta 0))'
    rule_body = '(assert (ficha (num ?n) (equipo "B") (pos-x ?x) ' \
                '(pos-y ?y) (puntos ?v) (descubierta 0)))'
    
    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_directo_1(module):
    rule_name = 'directo-1'
    rule_prec = '(declare (salience 10))' \
                '(tiempo ?t)' \
                '(equipoA ?t "A")' \
                '(ficha-r (num ?n) (equipo ?e) (pos-x ?x) ' \
                '(pos-y ?y) (puntos ?v) (descubierta 1))'
    rule_body = '(assert (ficha (num ?n) (equipo ?e) (pos-x ?x) ' \
                '(pos-y ?y) (puntos ?v) (descubierta 1)))'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_indirecto_0A(module):
    rule_name = 'indirecto-0A'
    rule_prec = '(declare (salience 10))' \
                '(tiempo ?t)' \
                '(equipoA ?t "B")' \
                '(ficha-r (num ?n) (equipo "A") (pos-x ?x) ' \
                '(pos-y ?y) (puntos ?v) (descubierta 0))'
    rule_body = '(assert (ficha (num ?n) (equipo "B") (pos-x (sim ?x)) ' \
                '(pos-y (sim ?y)) (puntos ?v) (descubierta 0)))'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_indirecto_0B(module):
    rule_name = 'indirecto-0B'
    rule_prec = '(declare (salience 10))' \
                '(tiempo ?t)' \
                '(equipoA ?t "B")' \
                '(ficha-r (num ?n) (equipo "B") (pos-x ?x) ' \
                '(pos-y ?y) (puntos ?v) (descubierta 0))'
    rule_body = '(assert (ficha (num ?n) (equipo "A") (pos-x (sim ?x)) ' \
                '(pos-y (sim ?y)) (puntos ?v) (descubierta 0)))'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_indirecto_1A(module):
    rule_name = 'indirecto-1A'
    rule_prec = '(declare (salience 10))' \
                '(tiempo ?t)' \
                '(equipoA ?t "B")' \
                '(ficha-r (num ?n) (equipo "A") (pos-x ?x) (pos-y ?y) ' \
                '(puntos ?v) (descubierta 1))'
    rule_body = '(assert (ficha (num ?n) (equipo "B") (pos-x (sim ?x)) ' \
                '(pos-y (sim ?y)) (puntos ?v) (descubierta 1)))'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_indirecto_1B(module):
    rule_name = 'indirecto-1B'
    rule_prec = '(declare (salience 10))' \
                '(tiempo ?t)' \
                '(equipoA ?t "B")' \
                '(ficha-r (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) ' \
                '(puntos ?v) (descubierta 1))'
    rule_body = '(assert (ficha (num ?n) (equipo "X") (pos-x (sim ?x)) ' \
                '(pos-y (sim ?y)) (puntos ?v) (descubierta 1)))'

    module.BuildRule(rule_name, rule_prec, rule_body)


class ClipsSubModuleTraducirFicha(clips_submodule.ClipsSubModule):

    def _define_submodule(self):
        submod_name = 'TRADUCIRF'
        submod_body = '(import MAIN deftemplate initial-fact ficha ficha-r ' \
                      'dimension tiempo)' \
                      '(import MAIN deffunction ?ALL)'

        self.module = self.parent.BuildModule(submod_name, submod_body)

    def __init__(self, parent):
        super(ClipsSubModuleTraducirFicha, self).__init__(parent)
        self.rules = {'inicial1-0': _clips_rule_inicial_1_0,
                      'inicial1-1': _clips_rule_inicial_1_1,
                      'inicial2': _clips_rule_inicial_2,
                      'elimina1': _clips_rule_elimina_1,
                      'elimina2': _clips_rule_elimina_2,
                      'directo-0A': _clips_rule_directo_0A,
                      'directo-0B': _clips_rule_directo_0B,
                      'directo-1': _clips_rule_directo_1,
                      'indirecto-0A': _clips_rule_indirecto_0A,
                      'indirecto-0B': _clips_rule_indirecto_0B,
                      'indirecto-1A': _clips_rule_indirecto_1A,
                      'indirecto-1B': _clips_rule_indirecto_1B}
