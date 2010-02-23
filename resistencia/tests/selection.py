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
This file contains a function to get all the installed teams
"""

import os

from resistencia import configure

def get_installed_teams():
    """
    Return a list of the installed teams. We consider a installed team some
    of the way 'data/teams/formations/equipoXX.clp',
    'data/teams/rules/reglasYYYY.clp' where XX == YYYY
    """
    base_path = configure.load_configuration()['se_path']
    rules_path = base_path + '/rules'
    formations_path = base_path + '/formations'

    list_rules = os.listdir(rules_path)
    list_formations = os.listdir(formations_path)

    for i in range(len(list_rules)):
        list_rules[i] = list_rules[i].replace('reglas','')
        list_rules[i] = list_rules[i].replace('.clp','')

    for i in range(len(list_formations)):
        list_formations[i] = list_formations[i].replace('equipo', '')
        list_formations[i] = list_formations[i].replace('.clp', '')

    set_rules = set(list_rules)
    set_formations = set(list_formations)

    set_final = set_rules.intersection(set_formations)
    list_final = list(set_final)

    res = []

    for i in range(len(list_final)):
        _rules = rules_path + '/reglas' + list_final[i] + '.clp'
        _form = formations_path + '/equipo' + list_final[i] + '.clp'
        res.append((_rules, _form))

    return res
