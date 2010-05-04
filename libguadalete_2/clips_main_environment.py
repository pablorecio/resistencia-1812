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

def _clips_main_templates():
    template_name = 'ficha-r'
    template_body = '(slot equipo)' \
                    '(slot num)' \
                    '(slot puntos)' \
                    '(slot pos-x)' \
                    '(slot pos-y)' \
                    '(slot descubierta)'
    clips.BuildTemplate(template_name, template_body)

    template_name = 'ficha'
    template_body = '(slot equipo)' \
                    '(slot num)' \
                    '(slot puntos)' \
                    '(slot pos-x)' \
                    '(slot pos-y)' \
                    '(slot descubierta)'
    clips.BuildTemplate(template_name, template_body)

    template_name = 'mueve'
    template_body = '(slot num)' \
                    '(slot mov)' \
                    '(slot tiempo)'
    clips.BuildTemplate(template_name, template_body)

class GuadaleteMainEnvironment:

    def __init__(self, num_turns=120, dimension=8, first_turn='A'):
        # self.parent = parent
        self.num_turns = num_turns
        self.dimension = dimension
        self.first_turn = first_turn
        self.base_a = 1
        self.base_b = dimension

        self.init = False

    def init_environment(self):
        # deffacts_body = '(tiempo-inicial {0})'.format(self.num_turns) \
        #                '(dimension {0})'.format(self.dimension) \
        #                '(turno "{0}")'.format(self.first_turn) \
        #                '(base "A" {0})'.format(self.base_a) \
        #                '(base "B" {0})'.format(self.base_b) \
        if not self.init:
            deffacts_name = 'opciones-juego'
            deffacts_body = '(tiempo-inicial {0})(dimension {1})(turno "{2}")' \
                            '(base "A" {3})' \
                            '(base "B" {4})' \
                            '(modulos INFORMAR TRADUCIRF EQUIPO-A MOVER ' \
                            'INFORMAR TRADUCIRF EQUIPO-B TRADUCIRM '\
                            'MOVER)'.format(self.num_turns,
                                            self.dimension,
                                            self.first_turn,
                                            self.base_a,
                                            self.base_b) 
            clips.BuildDeffacts(deffacts_name, deffacts_body)
            _clips_main_templates()

            self.init = True
        else: #check and throw exception
            pass
        
