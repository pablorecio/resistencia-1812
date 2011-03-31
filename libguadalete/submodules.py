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
# Copyright (C) 2010-2011, Pablo Recio Quijano,                               #
#                          <pablo.recioquijano@gmail.com>                     #
###############################################################################

import clips


class ClipsModule(object):
    def __init__(self, rules, module_name, module_body):
        self.rules = rules
        self.module = None
        self.module_name = module_name
        self.module_body = module_body

    def _define_submodule(self):
        # TODO - Extra validations
        self.module = clips.BuildModule(self.module_name, self.module_body)

    def clips_add_rule(self, function):
        # TODO - Checks the validation of the clips rule
        key, f = function

        if callable(f):
            self.rules[key] = f
        else:
            # TODO - Raise exception
            pass

    def clips_remove_rule(self, function_key):
        if function_key in self.rules:
            del self.rules[function_key]

    def clips_load_submodule(self):
        self._define_submodule()
        for key, (rule_name, rule_prec, rule_body) in self.rules.items():
            self.module.BuildRule(rule_name, rule_prec, rule_body)
