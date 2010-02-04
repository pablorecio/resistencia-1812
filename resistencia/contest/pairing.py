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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Copyright (C) 2010, Pablo Recio Quijano
#----------------------------------------------------------------------

import random

def _right_displacement(elements):
    """
    Function that do a circle displacement to the right. If elements is
    something like [1, 2, 3, 4], this function will return [4, 1, 2, 3]
    """
    n = len(elements)
    var_aux = elements[0]
    for i in range(n-1):
        elements[i+1], var_aux = var_aux, elements[i+1]

    elements[0] = var_aux
    return elements

def _rotate_less_first(elements):
    """
    This function do a circle displacement to the right, except the first
    element of the list. If elements is a list like [1, 2, 3, 4], this
    function will return [1, 4, 2, 3]
    """
    first = elements[0]
    rest = elements[1:]
    _right_displacement(rest)

    elements = rest
    elements.insert(0,first)
    return elements

def _get_pairing(elements):
    """
    Given an even list of elements, we return a list with the pairings of that
    list, using round-robin.

    If we recive a list [1, 2, 3, 4, 5, 6], the return list will be
    [(1, 6), (2, 5), (3, 4)]. This way prevents to repeat matchs on a contest
    """
    n = len(elements)

    pairing = []
    for i in range(n/2):
        pairing.append((elements[i],elements[n-i-1]))

    return pairing

def _generate_back_round(elements):
    """
    This function returns a list of reversed matchs. If a contest has the
    rounds assigned like [(1, 6), (2, 5), (3, 4)], will generete the reverse
    round as [(6, 1), (5, 2), (4, 3)]
    """
    matchs = []
    x = len(elements)
    y = len(elements[0])
    for i in range(x):
        aux = []
        for j in range(y):
            element = elements[i][j]
            aux.append((element[1], element[0]))
        matchs.append(aux)
    return matchs

def correct_pairing(matchs, back_round=False):
    """This function verifies the correction of a pairing.

    A pairing is not correct if two teams plays more than one time
    if it has no back round, or more than two times if it has back round.
    """
    x = len(matchs)
    y = len(matchs[0])
    band = True
    for i in range(x):
        for j in range(y):
            element = matchs[i][j]
            aux_list = [element]
            if back_round:
                element_i = element[1], element[0]
                aux_list.append(element_i)
            aux_set = set(aux_list)
            for k in range(x):
                s = set(matchs[k])
                res = s.intersection(aux_set)
                maxi = 0
                if i == k:
                    maxi = 1 
                if len(res) > maxi:
                    band = False

    return band

def make_pairings(teams, back_round=False):
    """This functions do the pairings using round-robin algorithm.

    Keywords arguments:
    teams -- list of teams names that participate on the contest
    back_round -- Boolean value that indicates if it's a two round contest

    Returns a list that contains lists of matchs, something like that:
    [[(a,d), (b,c)], [(a,c), (d,b)], [(a,b), (c,d)] 
    """
    random.shuffle(teams)
    
    #If has an odd number of teams, we have to add a ghost team
    if len(teams) % 2 == 1:
        teams.append('aux_ghost_team')

    first_order = teams
    elements = teams
    matchs = []

    finish = False #flag to control if we make the entire round

    while not finish:
        matchs.append(_get_pairing(elements))
        elements = _rotate_less_first(elements)
        if elements == first_order:
            finish = True

    if back_round: #the back round is the same but teams inverts
        matchs = matchs + _generate_back_round(matchs)

    return matchs

def test_pairing(main_team, teams, team_id = 0):
    random.shuffle(teams)

    matchs = []
    for team in teams:
        if team_id == 0:
            matchs.append((main_team, team))
        else:
            matchs.append((team, main_team))

    return matchs
