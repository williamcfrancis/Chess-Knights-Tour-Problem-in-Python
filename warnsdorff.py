import sys
board = []
board_size = -1
import sys
def initiateBoard (board_dimensions):
    global board
    global board_size
    global knights_moves
    board_size = board_dimensions
    for i in range(0, board_size):
        board.append(board_size*[0]) #untouched board

knights_moves = ((-2,-1),(1,2),(2,-1),(-2,1),(2,1),(-1,2),(1,-2),(-1,-2))

def isAvailable(x, y):
    if x < len(board) and y < len(board[0]) and \
       x >= 0 and y >= 0 and board[x][y]==0:
        return True
    else:
        return False

def getPossibleMoves(x, y):
     possible_moves = []
     for move in knights_moves: 
        cx,cy = x+move[0], y+move[1]
        if isAvailable(cx,cy):
            possible_moves.append((move[0],move[1]))
     return possible_moves  

def getNumMoves(x, y):
     return len(getPossibleMoves(x, y)) 
def drawBoard():
    for i in range(len(board)):
        print(board[i])
    return

    
def getNextMove (numMoves):
    smallestIndex = 0

    if numMoves==[]:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]==1:
                    mmin=(i,j)
                if board[i][j]==xxx*xxx:
                    mmax=(i,j)
        dif1=mmin[0]-mmax[0]
        dif2=mmin[1]-mmax[1]
        #print(dif1,dif2)
        if dif1<0:
            dif1*=-1
        if dif2<0:
            dif2*=-1
        #if (dif1==2 and dif2==1) or (dif1==1 and dif2==2):
        drawBoard()
        sys.exit()
        ##########################################
    else:
        smallest = numMoves[0]
        for i in range(len(numMoves)):
            if numMoves[i] < smallest:
                smallest = numMoves[i]
                smallestIndex = i

    return smallestIndex

def solve (x,y,num_move):
    
    assert board[x][y] == 0
    board[x][y] = num_move                                  
    possible_moves = getPossibleMoves(x,y)
    numOfMoves = []      
    for move in possible_moves:
        numOfMoves.append(getNumMoves(x+move[0],y+move[1]))
    nextMove = possible_moves[getNextMove(numOfMoves)]
    ############################################################
    if len(nextMove)==0:pass
    else:
        solve(x+nextMove[0],y+nextMove[1],num_move+1)


while True:
    print('''   USING WARNDSDORFF EURISTICS
1. OPEN Tour
2. CLOSED Tour
3. EXIT''')
    print('enter choice: ')
    ch=int(input(' '))
    if ch==1:
        xxx=int(input('enter dimensions: '))
        if xxx>=5:
            initiateBoard (xxx)
            solve(0,0,1)
            continue
        else:
            print('No Solution Exists')
    if ch==2:
        xxx=int(input('enter dimensions: '))
        if xxx>=5 and xxx%2==0:
            initiateBoard (xxx)
            solve(0,1,1)
            continue
        else:
            print('No Solution Exists')
    elif ch==3:
        sys.exit()
    else:
        print('invalid input. try again.')
