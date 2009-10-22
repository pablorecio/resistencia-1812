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

def _process_line(line):
    i = line.find("(") + 1
    elements = []

    while i != len(line) - 2:
        tmp1 = line.find("(",i)
        tmp2 = line.find(")",i) + 1
        elem = line[tmp1:tmp2]
        elements.append(elem)
        i = tmp2

    return elements

def _filter_line(line):
    for i in range(len(line)): #simply left the re-id
        if re.search('(equipo "A")',line[i]):
            line[i] = '(equipo "B")'
        if re.search('(pos-x .)',line[i]):
            line[i] = '(pos-x ' + _extract_x(line[i]) + ')'
        if re.search('(pos-y 1)',line[i]):
            line[i] = '(pos-y 8)'
        if re.search('(pos-y 2)',line[i]):
            line[i] = '(pos-y 7)'
    return line

def _extract_x(pos):
    n = pos[len(pos)-2]

    return str(int(n) - (-7 + 2 * (int(n) -1)))

def _get_line(elementos):
    sal = '(ficha-r'
    for i in elementos:
        print i
        if i == '':
            sal = sal + ')'
        else:
            sal = sal + ' ' + i
    sal = sal + ")\n"
    print sal
    return sal

def mirroring_team(src_file):
    f_team = open(src_file,"r")
    f_temp = open(team_path_tmp_file, "w")

    for l in f_team:
        if l[0] != ';' and len(l) > 30: #Assume it's a ficha-r definition
            piece = _process_line(l)
            filtered = _filter_line(piece)
            f_temp.write(_get_line(filtered))
        else:
            if re.search("deffacts",l):
                f_temp.write("(deffacts fichas-B\n")
            else:
                f_temp.write(l)
    
    return team_path_tmp_file

# Now functions that reverse the rules

def mirroring_rules(src_file):
    f_rule = open(src_file,"r")
    f_temp = open(rule_path_tmp_file, "w")

    for l in f_rule:
        #res = l.find("EQUIPO-A")
        #if res != -1:
        #    l[res+7] = 'B'
        f_temp.write(l.replace("EQUIPO-A", "EQUIPO-B"))
        

    return rule_path_tmp_file

                     
            
