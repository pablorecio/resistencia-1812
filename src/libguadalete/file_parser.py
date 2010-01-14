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

# Copyright (C) 2010, Pablo Recio Quijano
#----------------------------------------------------------------------

import os

max_value = 6

def __fill_matrix(x=8, y=8, value=0):
    m = []
    for i in range(x):
        f = []
        for j in range(y):
            f.append(value)
        m.append(f)
        
    return m

def __find_element_matrix(board, e):
    sum = 0
    for l in board:
        sum += l.count(e)

    return not sum == 0

def __define_winner(board):
    king_A = __find_element_matrix(board, 1)
    king_B = __find_element_matrix(board, -1)

    if (king_A and king_B) or (not king_A and not king_B):
        return 0
    elif king_A:
        return 1
    else:
        return -1

def parse_file(src_file):
    """
    This function allows to parse an output file generated on a simulation, and generate
    a data structure more computer readable.
    @param src_file File with a game played.
    @return A list with the boards for every single turn on a game.
    @todo See if it's the right place for this function
    """
    f = open(src_file)
    
    line = "0" #line value not null for the loop
    
    values = {}
    entire_game = []
    counter = 0
    
    while line != "":
        line = f.readline()
        if (line == "tiempo\n" or line == "fin\n"): #If we are in a new turn
            try: board
            except NameError:
                board = __fill_matrix()
            else:
                entire_game.append(board) #include the board on the game
                counter += 1
                del board
                board = __fill_matrix() #restart the board from 0
        else:
            if (line != "\n" and len(line) > 5):
                pos_e = line.find("e")
                pos_id = line.find("n")
                pos_val = line.find("p")
                pos_x = line.find("x")
                pos_y = line.find("y")
                pos_d = line.find("d")
                    
                e = line[pos_e+2:pos_id-1]
                id = line[pos_id+2:pos_val-1]
                val = line[pos_val+2:pos_x-1]
                x = line[pos_x+2:pos_y-1]
                y = line[pos_y+2:pos_d-1]
                d = line[pos_d+2:]
                
                values[id] = val
                
                if e == 'A':
                    board[int(y) - 1][int(x) - 1] = int(val) + (int(d)*max_value)
                else:
                    board[int(y) - 1][int(x) - 1] = int(val) - 2*int(val) - (int(d)*max_value)
                
    f.close()
    winner = __define_winner(entire_game[len(entire_game)-1])
    return entire_game, winner
