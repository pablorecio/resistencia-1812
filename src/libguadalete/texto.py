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
    # Show positions numbers on the board, to control best the movements
    #----------------------------------
    # Module name
    mod_name = "INFORMAR"
    # Module body
    mod_body  = "(import MAIN deftemplate initial-fact ficha-r dimension tiempo tiempo-inicial)"
    mod_body += "(import MAIN deffunction ?ALL)"
    # Building the module
    mod_informar = clips.BuildModule(mod_name, mod_body)
    #----------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'informacion'
    # Rule precontents
    rule_prec  = '(ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y) (descubierta ?d))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '(not (impresa ?e ?n ?t ?p))'
    # =>
    # Rule body
    rule_body  = '(assert (impresa ?e ?n ?t ?p))'
    rule_body += '(open "temporal.txt" fich "a")'
    rule_body += '(a-fichero-jugador ?e ?n ?p ?x ?y ?d)'
    rule_body += '(close fich)'
    # Building the rule
    informacion = mod_informar.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'inicial'
    # Rule precontents
    rule_prec  = '(declare (salience 100))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '(not (iniciado ?t))'
    rule_prec += '(dimension ?dim)'
    # =>
    # Rule body
    ### rule_body = '(printout t "*****" crlf)'
    rule_body  = '(open "temporal.txt" fich "a")'
    rule_body += '(a-fichero-tiempo ?t)'
    rule_body += '(close fich)'
    rule_body += '(assert (iniciado ?t))'
    rule_body += '(assert (fila (+ 1 ?dim)))'
    rule_body += '(assert (columna (+ 1 ?dim)))'
    # Building the rule
    inicial = mod_informar.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'vacia'
    # Rule precontents
    rule_prec  = '(declare (salience 10))'
    rule_prec += '?c <- (columna ?x)'
    rule_prec += '(fila ?y)'
    rule_prec += '(dimension ?dim)'
    rule_prec += '(test (not (> ?x ?dim)))'
    rule_prec += '(not (ficha-r (pos-x ?x) (pos-y ?y)))'
    # =>
    # Rule body
    rule_body  = '(retract ?c)'
    rule_body += '(assert (columna (+ ?x 1)))'
    ### rule_body += ='(printout t "(1)" crlf)'
    rule_body += '(printout t "    ")'
    # Building the rule
    vacia = mod_informar.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'noVacia'
    # Rule precontents
    rule_prec  = '(declare (salience 10))'
    rule_prec += '?c <- (columna ?x)'
    rule_prec += '(fila ?y)'
    rule_prec += '(dimension ?dim)'
    rule_prec += '(test (not (> ?x ?dim)))'
    rule_prec += '(ficha-r (equipo ?e) (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta ?d))'
    # =>
    # Rule body
    rule_body  = '(retract ?c)'
    rule_body += '(assert (columna (+ ?x 1)))'
    ### rule_body += '(printout t "(2)" crlf)'
    rule_body += '(printout t " " ?e ?v (valor ?d)))'
    # Building the rule
    no_vacia = mod_informar.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'siguienteFila'
    # Rule precontents
    rule_prec  = '(declare (salience 20))'
    rule_prec += '(dimension ?dim)'
    rule_prec += '?c <- (columna ?x)'
    rule_prec += '(test (> ?x ?dim))'
    rule_prec += '?f <- (fila ?y)'
    rule_prec += '(test (not (<= ?y 1)))'
    # =>
    # Rule body
    rule_body  = '(retract ?c ?f)'
    rule_body += '(assert (fila (- ?y 1)))'
    rule_body += '(assert (columna 1))'
    ### rule_body += '(printout t "(3)" crlf)'
    rule_body += '(printout t crlf (- ?y 1) "|")'
    # Building the rule
    siguiente_fila = mod_informar.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'finalFila'
    # Rule precontents
    rule_prec  = '(declare (salience 20))'
    rule_prec += '(dimension ?dim)'
    rule_prec += '?c <- (columna ?x)'
    rule_prec += '(test (> ?x ?dim))'
    rule_prec += '?f <- (fila ?y)'
    rule_prec += '(test (= 1 ?y))'
    # =>
    # Rule body
    rule_body  = '(retract ?c ?f)'
    ### rule_body += '(printout t "(4)" crlf)'
    rule_body += '(printout t crlf "----------------------------------" crlf '
    rule_body +=           '"x:  1   2   3   4   5   6   7   8" crlf)'
    ### rule_body += '(readline)'
    # Building the rule
    final_fila = mod_informar.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'fin1'
    # Rule precontents
    rule_prec  = '(declare (salience -100))'
    rule_prec += '(tiempo ?t&0)'
    # =>
    # Rule body
    rule_body  = '(printout t "Fin del tiempo" crlf)'
    rule_body += '(rename "temporal.txt" "resultado.txt")'
    # Building the rule
    fin1 = mod_informar.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'fin-sin-rey1'
    # Rule precontents
    rule_prec  = '(declare (salience -100))'
    rule_prec += '?c <- (tiempo ?t&~0)'
    rule_prec += '(not (ficha-r (equipo "A") (puntos 1)))'
    # =>
    # Rule body
    rule_body  = '(printout t "Rey del equipo A muerto" crlf)'
    rule_body += '(assert (rey-A-muerto))'
    rule_body += '(rename "temporal.txt" "resultado.txt")'
    # Building the rule
    fin_sin_rey1 = mod_informar.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'fin-sin-rey2'
    # Rule precontents
    rule_prec  = '(declare (salience -100))'
    rule_prec += '?c <- (tiempo ?t&~0)'
    rule_prec += '(not (ficha-r (equipo "B") (puntos 1)))'
    # =>
    # Rule body
    rule_body  = '(printout t "Rey del equipo B muerto" crlf)'
    rule_body += '(assert (rey-B-muerto))'
    rule_body += '(rename "temporal.txt" "resultado.txt")'
    # Building the rule
    fin_sin_rey2 = mod_informar.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------
