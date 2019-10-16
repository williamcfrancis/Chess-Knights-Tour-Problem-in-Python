import sys
Size = 0                                                                                                    # the board size, passed at runtime
board = []                                                                                                  # the board will be constructed as a list of lists

def main():
    global Size
    tsize=int(input("Enter size of board : "))
    Size = tsize                                                                                            # Default: Fill the normal 8x8 chess board
    for i in range(0, Size):
        board.append(Size*[0])                                                                              # Fill the board with zeroes
    Fill(0,0,1)                                                                                             # Start the recursion with a 1 in the upper left
    print("No solution found")                                                                              # if the recursion returns, it failed

def Validate(ty,tx):                                                                                        # check if coordinates are within the board
    return ty>=0 and tx>=0 and ty<Size and tx<Size and board[ty][tx] == 0                                   # and the square is empty

def Fill(y,x,counter):                                                                                      # The recursive function that fills the board
    assert board[y][x] == 0
    board[y][x] = counter                                                                                   # Fill the square
    if counter == Size*Size:                                                                                # Was this the last empty square?
        PrintBoard()                                                                                        # Yes, print the board...
        sys.exit(1)                                                                                         # ...and exit
    jumps = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))
    for jump in jumps:                                                                                      # otherwise, try all the empty neighbours in turn
        ty,tx = y+jump[0], x+jump[1]
        if Validate(ty,tx):
            Fill(ty,tx,counter+1)                                                                           # *** RECURSION! ***
    board[y][x] = 0                                                                                         # if we get here, all the neighbours failed,
                                                                                                            # so reset the square and return

def PrintBoard():                                                                                           # print the board using nice ASCII art ('+' and '-')
    scale = len(str(Size*Size))
    print(Size*("+" + scale*"-") + "+")
    for line in board:
        for elem in line:
            sys.stdout.write("|%*d" % (scale,elem))
        print("|\n"+Size*("+" + scale*"-") + "+")

if __name__ == "__main__":
    main()
    
