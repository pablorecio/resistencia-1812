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
team_inter_path_tmp_file = './equipoIntTemp.clp'
rule_path_tmp_file = './reglasTemporal.clp'

def _reverse_index(i):
    """
    Mathematical function that return the opposite index for given
    """
    return i - (-7 + 2 * (i - 1))

def mirroring_team(src_file):
    """Mirror the file for the formation of a team.
    
    Allows to invert a team from the A team to the B team.
    When the user generates the team formation file, the user thinks that
    the team will be on the bottom off the board, and his (1,1) coordinate
    is the actual (1,1) coordinate on the board.
    But if his team is the 'B' team the entire logic and formation will
    change. This function has the responsability to convert formation
    file to the B team, swapping the ubication ((1,1) is now (8,8)) and
    replacing A for B mostly.

    Keywords arguments:
    
    src_file -- Path to the original file
    
    Will return the path to the temporal file that has the new formation
    """
    f_team = open(src_file,"r")
    f_temp = open(team_path_tmp_file, "w")

    for l in f_team:
        print l
        l = l.replace('fichas-A', 'fichas-B')
        l = l.replace('(equipo "A")', '(equipo "B")')
        y = l.find('(pos-y') + 7
        if y > 30:
            l = l.replace('(pos-y ' + l[y] + ')',
                          '(pos-y ' + str(_reverse_index(int(l[y]))) + ')')
        x = l.find('(pos-x') + 7
        if x > 30:
            l = l.replace('(pos-x ' + l[x] + ')',
                          '(pos-x ' + str(_reverse_index(int(l[x]))) + ')')
        f_temp.write(l)
    
    return team_path_tmp_file

# Now functions that reverse the rules

def interactive_formation(src_file):
    f_team = open(src_file, 'r')
    f_temp = open(team_inter_path_tmp_file, 'w')

    for l in f_team:
        i = l.find('(num')
        if not i == -1:
            j = l.find(')', i)

            num_old = l[i+5:j]
            num = _convert_identifier(num_old)

            new_line = l.replace(num_old, num)
            #print new_line
        else:
            new_line = l
        f_temp.write(new_line)

    return team_inter_path_tmp_file

def mirroring_rules(src_file):
    """Mirror the file for the rules of a team.
    
    Function that convert rules for the A team to the B team.
    The same idea that mirroring_team, but in this case, works
    on the rule's file.

    Keywords arguments:
    
    src_file -- Path to the original file
    
    Will return the path to the temporal file that has the new rules
    """
    f_rule = open(src_file,"r")
    f_temp = open(rule_path_tmp_file, "w")

    for l in f_rule:
        f_temp.write(l.replace("EQUIPO-A", "EQUIPO-B"))
        
    return rule_path_tmp_file

                     
def _convert_identifier(old):
    new_id = ''
    for i in old:
        new_id += str(ord(i))

    return new_id
