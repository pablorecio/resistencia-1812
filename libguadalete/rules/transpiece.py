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
    'initial1-0': ('inicial1-0',
                   '(declare (salience 100))' \
                       '(tiempo ?t)',
                   '(printout t "**********************************" crlf )'),
    'initial1-1': ('inicial1-1',
                   '(declare (salience 100))' \
                       '(tiempo ?t)' \
                       '(test (= 0 (mod ?t 2)))',
                   '(assert (equipoA ?t "B"))'),
    'initial2': ('inicial2',
                 '(declare (salience 100))' \
                     '(tiempo ?t)' \
                     '(test (<> 0 (mod ?t 2)))',
                 '(assert (equipoA ?t "A"))'),
    'remove1': ('elimina1',
                '(declare (salience 20))' \
                    '(tiempo ?t)' \
                    '?h <- (ficha (num ?n) (equipo ?e) (pos-x ?x) ' \
                    '(pos-y ?y) (puntos ?v) (descubierta ?d))' \
                    '(not (limpia ?t))',
                '(retract ?h)'),
    'remove2': ('elimina2',
                '(declare (salience 19))' \
                    '(tiempo ?t)',
                '(printout t "*Limpiado" ?t  crlf)' \
                    '(assert (limpia ?t))'),
    'direct-0A': ('directo-0A',
                  '(declare (salience 10))' \
                      '(tiempo ?t)' \
                      '(equipoA ?t "A")' \
                      '(ficha-r (num ?n) (equipo "A") (pos-x ?x) ' \
                      '(pos-y ?y) (puntos ?v) (descubierta 0))',
                  '(assert (ficha (num ?n) (equipo "A") (pos-x ?x) ' \
                      '(pos-y ?y) (puntos ?v) (descubierta 0)))'),
    'direct-0B': ('directo-0B',
                  '(declare (salience 10))' \
                      '(tiempo ?t)' \
                      '(equipoA ?t "A")' \
                      '(ficha-r (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) ' \
                      '(puntos ?v) (descubierta 0))',
                  '(assert (ficha (num ?n) (equipo "B") (pos-x ?x) ' \
                      '(pos-y ?y) (puntos ?v) (descubierta 0)))'),
    'direct-1': ('directo-1',
                 '(declare (salience 10))' \
                     '(tiempo ?t)' \
                     '(equipoA ?t "A")' \
                     '(ficha-r (num ?n) (equipo ?e) (pos-x ?x) ' \
                     '(pos-y ?y) (puntos ?v) (descubierta 1))',
                 '(assert (ficha (num ?n) (equipo ?e) (pos-x ?x) ' \
                     '(pos-y ?y) (puntos ?v) (descubierta 1)))'),
    'indirect-0A': ('indirecto-0A',
                    '(declare (salience 10))' \
                        '(tiempo ?t)' \
                        '(equipoA ?t "B")' \
                        '(ficha-r (num ?n) (equipo "A") (pos-x ?x) ' \
                        '(pos-y ?y) (puntos ?v) (descubierta 0))',
                    '(assert (ficha (num ?n) (equipo "B") (pos-x (sim ?x)) ' \
                        '(pos-y (sim ?y)) (puntos ?v) (descubierta 0)))'),
    'indirect-0B': ('indirecto-0B',
                    '(declare (salience 10))' \
                        '(tiempo ?t)' \
                        '(equipoA ?t "B")' \
                        '(ficha-r (num ?n) (equipo "B") (pos-x ?x) ' \
                        '(pos-y ?y) (puntos ?v) (descubierta 0))',
                    '(assert (ficha (num ?n) (equipo "A") (pos-x (sim ?x)) ' \
                        '(pos-y (sim ?y)) (puntos ?v) (descubierta 0)))'),
    'indirect-1A': ('indirecto-1A',
                    '(declare (salience 10))' \
                        '(tiempo ?t)' \
                        '(equipoA ?t "B")' \
                        '(ficha-r (num ?n) (equipo "A") (pos-x ?x) (pos-y ?y) ' \
                        '(puntos ?v) (descubierta 1))',
                    '(assert (ficha (num ?n) (equipo "B") (pos-x (sim ?x)) ' \
                        '(pos-y (sim ?y)) (puntos ?v) (descubierta 1)))'),
    'indirect-1B': ('indirecto-1B',
                    '(declare (salience 10))' \
                        '(tiempo ?t)' \
                        '(equipoA ?t "B")' \
                        '(ficha-r (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) ' \
                        '(puntos ?v) (descubierta 1))',
                    '(assert (ficha (num ?n) (equipo "A") (pos-x (sim ?x)) ' \
                        '(pos-y (sim ?y)) (puntos ?v) (descubierta 1)))'),
}


module_name = 'TRADUCIRF'


module_body = '(import MAIN deftemplate initial-fact ficha ficha-r ' \
    'dimension tiempo)' \
    '(import MAIN deffunction ?ALL)'
