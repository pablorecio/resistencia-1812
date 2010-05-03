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

#from resistencia.nls import gettext as _

class ClipsSubModule(object):
    def __init__(self, parent):
        print 'Reciving {0} module as parent'.format(parent)
        self.rules = {}
        self.module = None
        self.parent = parent
        #self._define_submodule()
        #print 'Defined {0} module'.format(repr(self.module))
    
    def _define_submodule(self, parent):
        raise NotImplementedError('Base class. Method not implemented here')

    def clips_add_rule(self, function):
        # TODO - Checks the validation of the clips rule
        key = function[0]
        f = function[1]
        
        self.rules[key] = f

    def clips_remove_rule(self, function_key):
        # TODO - Catch exception
        del self.rules[function_key]

    def clips_load_submodule(self):
        self._define_submodule()
        print 'Defined {0} module'.format(repr(self.module))
        for k in self.rules:
            rule = self.rules[k]
            rule(self.module)
