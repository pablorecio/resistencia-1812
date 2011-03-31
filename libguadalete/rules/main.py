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
    'start-time': ('inicia-tiempo',
                   '(declare (salience 99))' \
                       '(not (tiempo-iniciado))' \
                       '(tiempo-inicial ?ti)',
                   '(assert (tiempo-iniciado))' \
                       '(assert (tiempo ?ti))'),
    'del-piece': ('borra-fich',
                  '(declare (salience 100))' \
                      '(not (fichero-abierto))',
                  '(printout t crlf "BORRANDO FICHERO" crlf)' \
                      '(assert (fichero-abierto))' \
                      '(open "temporal.txt" fich "w")' \
                      '(close fich)'),
    'control-and-time': ('control-y-tiempo',
                         '?c <- (tiempo ?t&~0)' \
                             '?orden <- (modulos INFORMAR $?r)',
                         '(retract ?c)' \
                             '(assert (tiempo (- ?t 1)))' \
                             '(retract ?orden)' \
                             '(assert (modulos $?r INFORMAR))' \
                             '(printout t "Pasamos al modulo INFORMAR." crlf)' \
                             '(printout t "Tiempo " ?t crlf)' \
                             '(focus INFORMAR)'),
    'control-w-time': ('control-sin-tiempo',
                       '?c <- (tiempo ?t&~0)' \
                           '?orden <- (modulos ?m&~INFORMAR $?r)' \
                           '(ficha-r (equipo "A") (puntos 1))' \
                           '(ficha-r (equipo "B") (puntos 1))',
                       '(retract ?orden)' \
                           '(printout t " Modulo->" ?m " ")' \
                           '(assert (modulos $?r ?m))' \
                           '(focus ?m)'),
}


module_name = 'MAIN'


module_body = '(export deftemplate initial-fact ficha ficha-r ' \
    'dimension tiempo mueve turno tiempo-inicial)' \
    '(export deffunction ?ALL)'
