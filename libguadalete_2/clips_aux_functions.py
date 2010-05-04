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

"""
This file contains the definition of functions used on the clips environment.
"""

import clips

def _clips_function_a_fichero_tiempo():
    # TODO - printout
    fun_name = 'a-fichero-tiempo'
    fun_para = '?t'
    fun_body = '(printout fich "tiempo" crlf ?t crlf)'

    clips.BuildFunction(fun_name, fun_para, fun_body)


def _clips_function_a_fichero_jugador():
    fun_name = 'a-fichero-jugador'
    fun_para = '?e ?n ?p ?x ?y ?d'
    fun_body = '(printout fich " e:" ?e)' \
               '(printout fich " n:" ?n)' \
               '(printout fich " p:" ?p)' \
               '(printout fich " x:" ?x)' \
               '(printout fich " y:" ?y)' \
               '(printout fich " d:" ?d)' \
               '(printout fich crlf)'

    clips.BuildFunction(fun_name, fun_para, fun_body)


def _clips_function_por_pantalla_jugador():
    fun_name = 'por-pantalla-jugador'
    fun_para = '?e ?n ?p ?x ?y ?d'
    fun_body = '(printout t "e:" ?e " n:" ?n " x:")' \
               '(if (< ?x 1000) then' \
               ' (printout t "0"))' \
               '(if (< ?x 100) then' \
               ' (printout t "0"))' \
               '(if (< ?x 10) then' \
               ' (printout t "0"))' \
               '(printout t ?x)' \
               '(printout t " y:")' \
               '(if (< ?y 1000) then' \
               ' (printout t "0"))' \
               '(if (< ?y 100) then' \
               ' (printout t "0"))' \
               '(if (< ?y 10) then' \
               ' (printout t "0"))' \
               '(printout t ?y crlf)'

    clips.BuildFunction(fun_name, fun_para, fun_body)


def _clips_function_distancia():
    fun_name = 'distancia'
    fun_para = '?x ?y ?x2 ?y2'
    fun_body = '(sqrt (+ (* (- ?x ?x2) (- ?x ?x2)) (* (- ?y ?y2) (- ?y ?y2))))'

    clips.BuildFunction(fun_name, fun_para, fun_body)


def _clips_function_dentro():
    fun_name = 'dentro'
    fun_para = '?x1 ?y1 ?x2 ?y2 ?x ?y'
    fun_body = '(and (or (<= ?x1 ?x ?x2) (>= ?x1 ?x ?x2))' \
               '(or (<= ?y1 ?y ?y2) (>= ?y1 ?y ?y2)))'

    clips.BuildFunction(fun_name, fun_para, fun_body)


def _clips_function_minimo():
    fun_name = 'minimo'
    fun_para = '?n1 ?n2'
    fun_body = '(if (< ?n1 ?n2) then ' \
               '?n1 ' \
               'else ' \
               '?n2)'

    clips.BuildFunction(fun_name, fun_para, fun_body)


def _clips_function_mov_x():
    fun_name = 'mov-x'
    fun_para = '?m'
    fun_body = '(switch ?m' \
               '(case 1 then 1)' \
               '(case 2 then -1)' \
               '(default 0))'

    clips.BuildFunction(fun_name, fun_para, fun_body)


def _clips_function_mov_y():
    fun_name = 'mov-y'
    fun_para = '?m'
    fun_body = '(switch ?m' \
               '(case 3 then 1)' \
               '(case 4 then -1)' \
               '(default 0))'

    clips.BuildFunction(fun_name, fun_para, fun_body)


def _clips_function_mov_valido():
    fun_name = 'mov-valido'
    fun_para = '?dim ?m ?x ?y'
    fun_body = '(and (> (+ ?x (mov-x ?m)) 0) (<= (+ ?x (mov-x ?m)) ?dim)' \
                    '(> (+ ?y (mov-y ?m)) 0) (<= (+ ?y (mov-y ?m)) ?dim))'

    clips.BuildFunction(fun_name, fun_para, fun_body)


def _clips_function_valor():
    fun_name = 'valor'
    fun_para = '?descubierto'
    fun_body = '(if (= 0 ?descubierto) then ' \
               '"?" ' \
               'else ' \
               '" ")'

    clips.BuildFunction(fun_name, fun_para, fun_body)


def _clips_function_simetrico():
    fun_name = 'simetrico'
    fun_para  = '?m'
    fun_body  = '(switch ?m' \
                '(case 1 then 2)' \
                '(case 2 then 1)' \
                '(case 3 then 4)' \
                '(case 4 then 3)' \
                '(default 0))'

    clips.BuildFunction(fun_name, fun_para, fun_body)


def _clips_function_sim():
    fun_name = 'sim'
    fun_para = '?p'
    fun_body  = '(- 9 ?p)'

    clips.BuildFunction(fun_name, fun_para, fun_body)


def _clips_function_turno():
    fun_name = 'turno'
    fun_para = '?ti ?ta'
    fun_body = '(if (= (mod (- ?ti ?ta) 2) 1) then ' \
               '"A" ' \
               'else ' \
               '"B") '

    clips.BuildFunction(fun_name, fun_para, fun_body)


__functions__ = {'a-fichero-tiempo': _clips_function_a_fichero_tiempo,
                 'a-fichero-jugador': _clips_function_a_fichero_jugador,
                 'por-pantalla-jugador': _clips_function_por_pantalla_jugador,
                 'distancia': _clips_function_distancia,
                 'dentro': _clips_function_dentro,
                 'minimo': _clips_function_minimo,
                 'mov-x': _clips_function_mov_x,
                 'mov-y': _clips_function_mov_y,
                 'valor': _clips_function_valor,
                 'simetrico': _clips_function_simetrico,
                 'sim': _clips_function_sim,
                 'turno': _clips_function_turno,
                 'mov-valido': _clips_function_mov_valido}


def register_clips_functions():
    #global __clips__
    #__clips__ = parent
    for k in __functions__:
        print 'Registring {0} function'.format(k)
        function = __functions__[k]
        function()
