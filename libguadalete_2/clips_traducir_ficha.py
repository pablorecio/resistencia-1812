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

import clips

import clips_submodule

def _clips_rule_inicial_1_0(module):
    # TODO - printout
    rule_name = 'inicial1-0'
    rule_prec = '(declare (salience 100))' \
                '(tiempo ?t)'
    rule_body = '(printout t "**********************************" crlf )'

    module.BuildRule(rule_name, rule_prec, rule_body)


def _clips_rule_inicial_1_1(module):
    # TODO - printout
    rule_name = 'inicial1-1'
    rule_prec = '(declare (salience 100))' \
                '(tiempo ?t)' \
                '(test (= 0 (mod ?t 2)))'
    rule_body = '(assert (equipoA ?t "B"))'

    module.BuildRule(rule_name, rule_prec, rule_body)


class ClipsSubModuleTraducirFicha(clips_submodule.ClipsSubModule):

    def _define_submodule(self):
        submod_name = 'TRADUCIRF'
        submod_body = '(import MAIN deftemplate initial-fact ficha ficha-r ' \
                      'dimension tiempo)' \
                      '(import MAIN deffunction ?ALL)'

        self.module = clips.BuildModule(submod_name, submod_body)

    def __init__(self):
        super(ClipsSubModuleTraducirFicha, self).__init__()
        self.rules = {}
