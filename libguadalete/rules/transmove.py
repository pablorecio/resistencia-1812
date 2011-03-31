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


rules = {'translate': ('traducir',
                       '(declare (salience 10))' \
                           '(tiempo ?t)' \
                           '?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))' \
                           '(tiempo-inicial ?ti)' \
                           '(test (= 0 (str-compare (turno ?ti ?t) "B")))' \
                           '(ficha-r (equipo "B") (num ?n))' \
                           '(not (traducido ?n ?t))',
                       '(retract ?h1)' \
                           '(printout t "Traducido mov ficha-r n" ?n "de  "?m" a " ' \
                           '(simetrico ?m) crlf)' \
                           '(assert (traducido ?n ?t))' \
                           '(assert (mueve (num ?n) (mov (simetrico ?m)) (tiempo ?t)))')}


module_name = 'TRADUCIRM'


module_body = '(import MAIN deftemplate initial-fact ficha ficha-r ' \
    'dimension tiempo mueve tiempo-inicial)' \
    '(import MAIN deffunction ?ALL)'
