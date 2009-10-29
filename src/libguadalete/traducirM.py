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
    mod_name = "TRADUCIRM"
    # Module body
    mod_body  = "(import MAIN deftemplate initial-fact ficha ficha-r dimension tiempo mueve tiempo-inicial)"
    mod_body += "(import MAIN deffunction ?ALL)"
    # Building the module
    mod_traducirM = clips.BuildModule(mod_name, mod_body)
    #----------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'traducir'
    # Rule precontents
    rule_prec  = '(declare (salience 10))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))'
    rule_prec += '(tiempo-inicial ?ti)'
    rule_prec += '(test (= 0 (str-compare (turno ?ti ?t) "B")))'
    rule_prec += '(ficha-r (equipo "B") (num ?n))'
    rule_prec += '(not (traducido ?n ?t))'
    # =>
    # Rule body
    rule_body  = '(retract ?h1)'
    rule_body += '(printout t "Traducido mov ficha-r n" ?n "de  "?m" a " (simetrico ?m) crlf)'
    ### rule_body += '(printout t "turno de " ?ti " y " ?t " vale " (turno ?ti ?t) " y su str-compare con B da " (str-compare (turno ?ti ?t) "B"))'
    rule_body += '(assert (traducido ?n ?t))'
    rule_body += '(assert (mueve (num ?n) (mov (simetrico ?m)) (tiempo ?t)))'
    # Building the rule
    traducir = mod_traducirM.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------
