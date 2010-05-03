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

import clips_submodule


def _clips_rule_inicia_tiempo(module):
    rule_name = 'inicia-tiempo'
    rule_prec = '(declare (salience 99))' \
                '(not (tiempo-iniciado))' \
                '(tiempo-inicial ?ti)'
    rule_body = '(assert (tiempo-iniciado))' \
                '(assert (tiempo ?ti))'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_borra_fich(module):
    # TODO - printout y trabajo con el fichero
    rule_name = 'borra-fich'
    rule_prec = '(declare (salience 100))' \
                '(not (fichero-abierto))'
    rule_body = '(printout t crlf "BORRANDO FICHERO" crlf)' \
                '(assert (fichero-abierto))' \
                '(open "temporal.txt" fich "w")' \
                '(close fich)'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_control_y_tiempo(module):
    # TODO - printout
    rule_name = 'control-y-tiempo'
    rule_prec = '?c <- (tiempo ?t&~0)' \
                '?orden <- (modulos INFORMAR $?r)'
    rule_body = '(retract ?c)' \
                '(assert (tiempo (- ?t 1)))' \
                '(retract ?orden)' \
                '(assert (modulos $?r INFORMAR))' \
                '(printout t "Pasamos al modulo INFORMAR." crlf)' \
                '(printout t "Tiempo " ?t crlf)' \
                '(focus INFORMAR)'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_control_sin_tiempo(module):
    rule_name = 'control-sin-tiempo'
    rule_prec = '?c <- (tiempo ?t&~0)' \
                '?orden <- (modulos ?m&~INFORMAR $?r)' \
                '(ficha-r (equipo "A") (puntos 1))' \
                '(ficha-r (equipo "B") (puntos 1))'
    rule_body  = '(retract ?orden)' \
                 '(printout t " Modulo->" ?m " ")' \
                 '(assert (modulos $?r ?m))' \
                 '(focus ?m)'

    module.BuildRule(rule_name, rule_prec, rule_body)


class ClipsSubModuleMain(clips_submodule.ClipsSubModule):

    def _define_submodule(self):
        submod_name = 'MAIN'
        submod_body = '(export deftemplate initial-fact ficha ficha-r ' \
                      'dimension tiempo mueve turno tiempo-inicial)' \
                      '(export deffunction ?ALL)'

        self.module = self.parent.BuildModule(submod_name, submod_body)

    def __init__(self, parent):
        super(ClipsSubModuleMain, self).__init__(parent)
        self.rules = {'inicia-tiempo': _clips_rule_inicia_tiempo,
                      'borra-fich': _clips_rule_borra_fich,
                      'control_y_tiempo': _clips_rule_control_y_tiempo,
                      'control-sin-tiempo': _clips_rule_control_sin_tiempo}
