# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# This file is part of Resistencia Cadiz 1812.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Copyright (C) 2009, Pablo Recio Quijano
#----------------------------------------------------------------------

import re

team_path_tmp_file = './equipoTemporal.clp'
rule_path_tmp_file = './reglasTemporal.clp'

def _reverse_index(i):
    return i - (-7 + 2 * (i - 1))

def mirroring_team(src_file):
    f_team = open(src_file,"r")
    f_temp = open(team_path_tmp_file, "w")

    for l in f_team:
        print l
        l = l.replace('fichas-A', 'fichas-B')
        l = l.replace('(equipo "A")', '(equipo "B")')
        y = l.find('(pos-y') + 7
        if y > 30:
            l = l.replace('(pos-y ' + l[y] + ')', '(pos-y ' + str(_reverse_index(int(l[y]))) + ')')
        x = l.find('(pos-x') + 7
        if x > 30:
            l = l.replace('(pos-x ' + l[x] + ')', '(pos-x ' + str(_reverse_index(int(l[x]))) + ')')
        f_temp.write(l)
    
    return team_path_tmp_file

# Now functions that reverse the rules

def mirroring_rules(src_file):
    f_rule = open(src_file,"r")
    f_temp = open(rule_path_tmp_file, "w")

    for l in f_rule:
        f_temp.write(l.replace("EQUIPO-A", "EQUIPO-B"))
        

    return rule_path_tmp_file

                     
            
