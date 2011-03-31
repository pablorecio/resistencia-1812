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


functions = [
    ('a-fichero-tiempo',
     '?t',
     '(printout fich "tiempo" crlf ?t crlf)'),
    ('a-fichero-jugador',
     '?e ?n ?p ?x ?y ?d',
     '(printout fich " e:" ?e)' \
         '(printout fich " n:" ?n)' \
         '(printout fich " p:" ?p)' \
         '(printout fich " x:" ?x)' \
         '(printout fich " y:" ?y)' \
         '(printout fich " d:" ?d)' \
         '(printout fich crlf)'),
    ('por-pantalla-jugador',
     '?e ?n ?p ?x ?y ?d',
     '(printout t "e:" ?e " n:" ?n " x:")' \
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
         '(printout t ?y crlf)'),
    ('distancia',
     '?x ?y ?x2 ?y2',
     '(sqrt (+ (* (- ?x ?x2) (- ?x ?x2)) (* (- ?y ?y2) (- ?y ?y2))))'),
    ('dentro',
     '?x1 ?y1 ?x2 ?y2 ?x ?y',
     '(and (or (<= ?x1 ?x ?x2) (>= ?x1 ?x ?x2))' \
         '(or (<= ?y1 ?y ?y2) (>= ?y1 ?y ?y2)))'),
    ('minimo',
     '?n1 ?n2',
     '(if (< ?n1 ?n2) then ' \
         '?n1 ' \
         'else ' \
         '?n2)'),
    ('mov-x',
     '?m',
     '(switch ?m' \
         '(case 1 then 1)' \
         '(case 2 then -1)' \
         '(default 0))'),
    ('mov-y',
     '?m',
     '(switch ?m' \
         '(case 3 then 1)' \
         '(case 4 then -1)' \
         '(default 0))'),
    ('mov-valido',
     '?dim ?m ?x ?y',
     '(and (> (+ ?x (mov-x ?m)) 0) (<= (+ ?x (mov-x ?m)) ?dim)' \
         '(> (+ ?y (mov-y ?m)) 0) (<= (+ ?y (mov-y ?m)) ?dim))'),
    ('valor',
     '?descubierto',
     '(if (= 0 ?descubierto) then ' \
         '"?" ' \
         'else ' \
         '" ")'),
    ('simetrico',
     '?m',
     '(switch ?m' \
         '(case 1 then 2)' \
         '(case 2 then 1)' \
         '(case 3 then 4)' \
         '(case 4 then 3)' \
         '(default 0))'),
    ('sim',
     '?p',
     '(- 9 ?p)'),
    ('turno',
     '?ti ?ta',
     '(if (= (mod (- ?ti ?ta) 2) 1) then ' \
         '"A" ' \
         'else ' \
         '"B") '),
    ]
