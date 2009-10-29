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
 @file fB.py
"""

def LoadFunctions(clips):
    # Module name
    mod_name = "EQUIPO-B"
    # Module body
    mod_body  = "(import MAIN deftemplate initial-fact ficha dimension tiempo mueve tiempo-inicial)"
    mod_body += "(import MAIN deffunction ?ALL)"
    # Building the module
    mod_equipoB = clips.BuildModule(mod_name, mod_body)
    #---------------------------------

    # --------------------------------
    # Next rules have minimun priority, so it's only played if
    # the team has no rules to apply at this moment
    # ---------------------------------
    # Rule name
    rule_name = 'basica1'
    # Rule precontents
    rule_prec  = '(declare (salience 1))'
    rule_prec += '(tiempo ?t)'
    ### rule_prec += '(not (movido-B ?t))'
    rule_prec += '(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y))'
    rule_prec += '(dimension ?dim&:(< ?x (+ 1 (/ ?dim 2))))'
    rule_prec += '(not (ficha (equipo "A") (pos-x ?x2&:(= ?x2 (+ ?x 1))) (pos-y ?y)))'
    # =>
    # Rule body
    rule_body  = '(printout t "EQUIPO-B mueve a" ?n " hacia 1 en t " ?t crlf)'
    rule_body += '(assert (mueve (num ?n) (mov 1) (tiempo ?t)))'
    # Building the rule
    basica1B = mod_equipoB.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------
    
    # ---------------------------------
    # Rule name
    rule_name = 'basica2'
    # Rule precontents
    rule_prec  = '(declare (salience 1))'
    rule_prec += '(tiempo ?t)'
    ### rule_prec += '(not (movido-B ?t))'
    rule_prec += '(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y))'
    rule_prec += '(dimension ?dim&:(> ?x (+ 1 (/ ?dim 2))))'
    rule_prec += '(not (ficha (equipo "A") (pos-x ?x2&:(= ?x2 (- ?x 1))) (pos-y ?y)))'
    # =>
    # Rule body
    rule_body  = '(printout t "EQUIPO-B mueve a" ?n " hacia 2 en t " ?t crlf)'
    rule_body += '(assert (mueve (num ?n) (mov 2) (tiempo ?t)))'
    # Building the rule
    basica2B = mod_equipoB.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------
    
    # ---------------------------------
    # Rule name
    rule_name = 'basica3'
    # Rule precontents
    rule_prec  = '(declare (salience 1))'
    rule_prec += '(tiempo ?t)'
    ### rule_prec += '(not (movido-B ?t))'
    rule_prec += '(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y))'
    rule_prec += '(dimension ?dim&:(< ?y (+ 1 (/ ?dim 2))))'
    rule_prec += '(not (ficha (equipo "A") (pos-x ?x) (pos-y ?y2&:(= ?y2 (+ ?y 1)))))'
    ### rule_prec += '(not (ficha (equipo "A") (pos-x ?x) (pos-y (+ ?y 1))))'
    # =>
    # Rule body
    rule_body  = '(printout t "EQUIPO-B mueve a" ?n " hacia 3 en t " ?t crlf)'
    rule_body += '(assert (mueve (num ?n) (mov 3) (tiempo ?t)))'
    # Building the rule
    basica3B = mod_equipoB.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------
    
    # ---------------------------------
    # Rule name
    rule_name = 'basica4'
    # Rule precontents
    rule_prec  = '(declare (salience 1))'
    rule_prec += '(tiempo ?t)'
    ### rule_prec += '(not (movido-B ?t))'
    rule_prec += '(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y))'
    rule_prec += '(dimension ?dim&:(> ?y (+ 1 (/ ?dim 2))))'
    rule_prec += '(not (ficha (equipo "A") (pos-x ?x) (pos-y ?y2&:(= ?y2 (- ?y 1)))))'
    ### rule_prec += '(not (ficha (equipo "A") (pos-x ?x) (pos-y (- ?y 1))))'
    # =>
    # Rule body
    rule_body  = '(printout t "EQUIPO-B mueve a" ?n " hacia 4 en t " ?t crlf)'
    rule_body += '(assert (mueve (num ?n) (mov 4) (tiempo ?t)))'
    # Building the rule
    basica4B = mod_equipoB.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------
    
    # ---------------------------------
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
    terminaB = mod_equipoB.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------
