"""
This module includes a function to parse an original output from 
the CLIPS scripts. Those files have the form:
tiempo
199
e:<TEAM> n:<ID> p:<VALUE> x:<X> y:<Y> d:<UNCOVER>
...
...
tiempo
198
...
...

And so on until 'fin' at the end of the fle. Each line has the values
of an individual piece, such as in what team works, the ID number, etc...
"""

import matrixBoard

def fillMatrix():
    """
    """
    board = matrixBoard.Matrix(8,8)
    for i in range(8*8):
        x = (i/8)+1
        y = (i%8)+1
        board.setitem(x,y,'    ')

    return board
    


def parseFile(srcFile):
    "The return of this function is a list with N boards, where N is the number of turns of the game. This way, another module can read the list for a properly output"
    f = open(srcFile)

    line = "0" #line value not null for the loop
    
    values = {}
    entireGame = []
    counter = 0

    while line != "":
        line = f.readline()
        if (line == "tiempo\n" or line == "fin\n"): #If we are in a new turn
            try: board
            except NameError:
                board = fillMatrix()
            else:
                entireGame.append(board) #include the board on the game
                counter += 1
                del board
                board = fillMatrix() #restart the board from 0
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
                
                board.setitem(int(y),int(x),'['+e+val+']')
                
    f.close()

    return entireGame
