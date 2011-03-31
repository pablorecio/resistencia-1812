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
 @file funciones.clp
 Contains function definition that should be usefull to develop strategies
"""

def LoadFunctions(clips):
    # ---------------------------------
    # Function name
    fun_name = 'a-fichero-tiempo'
    # Function parameters
    fun_para  = '?t'
    # Function body
    fun_body  = '(printout fich "tiempo" crlf ?t crlf)'
    # Building the function
    a_fichero_tiempo = clips.BuildFunction(fun_name, fun_para, fun_body)
    # ---------------------------------

    # ---------------------------------
    # Function name
    fun_name = 'a-fichero-jugador'
    # Function parameters
    fun_para  = '?e ?n ?p ?x ?y ?d'
    # Function body
    ### fun_body = '(open "temporal.txt" fich "a")'
    fun_body  = '(printout fich " e:" ?e)'
    fun_body += '(printout fich " n:" ?n)'
    fun_body += '(printout fich " p:" ?p)'
    fun_body += '(printout fich " x:" ?x)'
    fun_body += '(printout fich " y:" ?y)'
    fun_body += '(printout fich " d:" ?d)'
    fun_body += '(printout fich crlf)'
    ### fun_body += '(close fich)'
    # Building the function
    a_fichero_jugador = clips.BuildFunction(fun_name, fun_para, fun_body)
    # ---------------------------------

    # ---------------------------------
    # Function name
    fun_name = 'por-pantalla-jugador'
    # Function parameters
    fun_para  = '?e ?n ?p ?x ?y ?d'
    # Function body
    fun_body  = '(printout t "e:" ?e " n:" ?n " x:")'
    fun_body += '(if (< ?x 1000) then'
    fun_body +=   '(printout t "0"))'
    fun_body += '(if (< ?x 100) then'
    fun_body +=   '(printout t "0"))'
    fun_body += '(if (< ?x 10) then'
    fun_body +=   '(printout t "0"))'
    fun_body += '(printout t ?x)'
    fun_body += '(printout t " y:")'
    fun_body += '(if (< ?y 1000) then'
    fun_body +=   '(printout t "0"))'
    fun_body += '(if (< ?y 100) then'
    fun_body +=   '(printout t "0"))'
    fun_body += '(if (< ?y 10) then'
    fun_body +=   '(printout t "0"))'
    fun_body += '(printout t ?y crlf)'
    # Building the function
    por_pantalla_jugador = clips.BuildFunction(fun_name, fun_para, fun_body)
    # ---------------------------------

    # ---------------------------------
    # Function name
    fun_name = 'distancia'
    # Function parameters
    fun_para  = '?x ?y ?x2 ?y2'
    # Function body
    fun_body  = '(sqrt (+ (* (- ?x ?x2) (- ?x ?x2)) (* (- ?y ?y2) (- ?y ?y2))))'
    # Building the function
    distancia = clips.BuildFunction(fun_name, fun_para, fun_body)
    # ---------------------------------

    # ---------------------------------
    # Function name
    fun_name = 'dentro'
    # Function parameters
    fun_para  = '?x1 ?y1 ?x2 ?y2 ?x ?y'
    # Function body
    fun_body  = '(and (or (<= ?x1 ?x ?x2) (>= ?x1 ?x ?x2))'
    fun_body +=      '(or (<= ?y1 ?y ?y2) (>= ?y1 ?y ?y2)))'
    # Building the function
    dentro = clips.BuildFunction(fun_name, fun_para, fun_body)
    # ---------------------------------

    # ---------------------------------
    # Function name
    fun_name = 'minimo'
    # Function parameters
    fun_para  = '?n1 ?n2'
    # Function body
    fun_body  = '(if (< ?n1 ?n2) then '
    fun_body +=   '?n1 '
    fun_body +=   'else '
    fun_body +=   '?n2)'
    # Building the function
    minimo = clips.BuildFunction(fun_name, fun_para, fun_body)
    # ---------------------------------

    # ---------------------------------
    # Function name
    fun_name = 'mov-x'
    # Function parameters
    fun_para  = '?m'
    # Function body
    fun_body  = '(switch ?m'
    fun_body +=         '(case 1 then 1)'
    fun_body +=         '(case 2 then -1)'
    fun_body +=         '(default 0))'
    # Building the function
    mov_x = clips.BuildFunction(fun_name, fun_para, fun_body)
    # ---------------------------------

    # ---------------------------------
    # Function name
    fun_name = 'mov-y'
    # Function parameters
    fun_para  = '?m'
    # Function body
    fun_body  = '(switch ?m'
    fun_body +=         '(case 3 then 1)'
    fun_body +=         '(case 4 then -1)'
    fun_body +=         '(default 0))'
    # Building the function
    mov_y = clips.BuildFunction(fun_name, fun_para, fun_body)
    # ---------------------------------

    # ---------------------------------
    # Function name
    fun_name = 'mov-valido'
    # Function parameters
    fun_para  = '?dim ?m ?x ?y'
    # Function body
    fun_body  = '(and (> (+ ?x (mov-x ?m)) 0) (<= (+ ?x (mov-x ?m)) ?dim)'
    fun_body +=      '(> (+ ?y (mov-y ?m)) 0) (<= (+ ?y (mov-y ?m)) ?dim))'
    # Building the function
    non_valido = clips.BuildFunction(fun_name, fun_para, fun_body)
    # ---------------------------------

    # ---------------------------------
    # Function name
    fun_name = 'valor'
    # Function parameters
    fun_para  = '?descubierto'
    # Function body
    fun_body  = '(if (= 0 ?descubierto) then '
    fun_body +=   '"?" '
    fun_body +=   'else '
    fun_body +=   '" ")'
    # Building the function
    valor = clips.BuildFunction(fun_name, fun_para, fun_body)
    # ---------------------------------

    # ---------------------------------
    # Function name
    fun_name = 'simetrico'
    # Function parameters
    fun_para  = '?m'
    # Function body
    fun_body  = '(switch ?m'
    fun_body +=         '(case 1 then 2)'
    fun_body +=         '(case 2 then 1)'
    fun_body +=         '(case 3 then 4)'
    fun_body +=         '(case 4 then 3)'
    fun_body +=         '(default 0))'
    # Building the function
    simetrico = clips.BuildFunction(fun_name, fun_para, fun_body)
    # ---------------------------------

    # ---------------------------------
    # Function name
    fun_name = 'sim'
    # Function parameters
    fun_para  = '?p'
    # Function body
    fun_body  = '(- 9 ?p)'
    # Building the function
    sim = clips.BuildFunction(fun_name, fun_para, fun_body)
    # ---------------------------------

    # ---------------------------------
    # Function name
    fun_name = 'turno'
    # Function parameters
    fun_para  = '?ti ?ta'
    # Function body
    fun_body  = '(if (= (mod (- ?ti ?ta) 2) 1) then '
    fun_body +=     '"A" '
    fun_body +=     'else '
    fun_body +=     '"B") '
    # Building the function
    turno = clips.BuildFunction(fun_name, fun_para, fun_body)
    # ----------------------------------


