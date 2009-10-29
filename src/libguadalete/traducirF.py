# -*- coding: utf-8 -*-
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

# Copyright (C) 2007, Manuel Palomo Duarte
# Copyright (C) 2009, Pablo Recio Quijano
#----------------------------------------------------------------------

"""
 @file texto.py
"""

def LoadFunctions(clips):
    #----------------------------------
    # Module name
    mod_name = "TRADUCIRF"
    # Module body
    mod_body  = "(import MAIN deftemplate initial-fact ficha ficha-r dimension tiempo)"
    mod_body += "(import MAIN deffunction ?ALL)"
    # Building the module
    mod_traducirF = clips.BuildModule(mod_name, mod_body)
    #----------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'inicial1-0'
    # Rule precontents
    rule_prec  = '(declare (salience 100))'
    rule_prec += '(tiempo ?t)'
    # =>
    # Rule body
    rule_body  = '(printout t "**********************************" crlf )'
    # Building the rule
    inicial1_0 = mod_traducirF.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'inicial1-1'
    # Rule precontents
    rule_prec  = '(declare (salience 100))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '(test (= 0 (mod ?t 2)))'
    # =>
    # Rule body
    rule_body  = '(assert (equipoA ?t "B"))'
    # Building the rule
    inicial1_1 = mod_traducirF.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'inicial2'
    # Rule precontents
    rule_prec  = '(declare (salience 100))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '(test (<> 0 (mod ?t 2)))'
    # =>
    # Rule body
    rule_body  = '(assert (equipoA ?t "A"))'
    # Building the rule
    inicial1_1 = mod_traducirF.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'elimina1'
    # Rule precontents
    rule_prec  = '(declare (salience 20))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '?h <- (ficha (num ?n) (equipo ?e) (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta ?d))'
    rule_prec += '(not (limpia ?t))'
    # =>
    # Rule body
    rule_body  = '(retract ?h)'
    # Building the rule
    elimina1 = mod_traducirF.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'elimina2'
    # Rule precontents
    rule_prec  = '(declare (salience 19))'
    rule_prec += '(tiempo ?t)'
    # =>
    # Rule body
    rule_body  = '(printout t "*Limpiado" ?t  crlf)'
    rule_body += '(assert (limpia ?t))'
    # Building the rule
    elimina2 = mod_traducirF.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'directo-0A'
    # Rule precontents
    rule_prec  = '(declare (salience 10))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '(equipoA ?t "A")'
    rule_prec += '(ficha-r (num ?n) (equipo "A") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0))'
    # =>
    # Rule body
    rule_body  = '(assert (ficha (num ?n) (equipo "A") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0)))'
    # Building the rule
    directo_0A = mod_traducirF.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'directo-0B'
    # Rule precontents
    rule_prec  = '(declare (salience 10))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '(equipoA ?t "A")'
    rule_prec += '(ficha-r (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0))'
    # =>
    # Rule body
    rule_body  = '(assert (ficha (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0)))'
    # Building the rule
    directo_0B = mod_traducirF.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'directo-1'
    # Rule precontents
    rule_prec  = '(declare (salience 10))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '(equipoA ?t "A")'
    rule_prec += '(ficha-r (num ?n) (equipo ?e) (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 1))'
    # =>
    # Rule body
    rule_body  = '(assert (ficha (num ?n) (equipo ?e) (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 1)))'
    # Building the rule
    directo_1 = mod_traducirF.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'indirecto-0A'
    # Rule precontents
    rule_prec  = '(declare (salience 10))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '(equipoA ?t "B")'
    rule_prec += '(ficha-r (num ?n) (equipo "A") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0))'
    # =>
    # Rule body
    rule_body  = '(assert (ficha (num ?n) (equipo "B") (pos-x (sim ?x)) (pos-y (sim ?y)) (puntos ?v) (descubierta 0)))'
    # Building the rule
    indirecto_0A = mod_traducirF.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'indirecto-0B'
    # Rule precontents
    rule_prec  = '(declare (salience 10))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '(equipoA ?t "B")'
    rule_prec += '(ficha-r (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0))'
    # =>
    # Rule body
    rule_body  = '(assert (ficha (num ?n) (equipo "A") (pos-x (sim ?x)) (pos-y (sim ?y)) (puntos ?v) (descubierta 0)))'
    # Building the rule
    indirecto_0B = mod_traducirF.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'indirecto-1A'
    # Rule precontents
    rule_prec  = '(declare (salience 10))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '(equipoA ?t "B")'
    rule_prec += '(ficha-r (num ?n) (equipo "A") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 1))'
    # =>
    # Rule body
    rule_body  = '(assert (ficha (num ?n) (equipo "B") (pos-x (sim ?x)) (pos-y (sim ?y)) (puntos ?v) (descubierta 1)))'
    # Building the rule
    indirecto_1A = mod_traducirF.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'indirecto-1B'
    # Rule precontents
    rule_prec  = '(declare (salience 10))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '(equipoA ?t "B")'
    rule_prec += '(ficha-r (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 1))'
    # =>
    # Rule body
    rule_body  = '(assert (ficha (num ?n) (equipo "A") (pos-x (sim ?x)) (pos-y (sim ?y)) (puntos ?v) (descubierta 1)))'
    # Building the rule
    indirecto_1B = mod_traducirF.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    
