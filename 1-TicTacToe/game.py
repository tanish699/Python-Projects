
# Initial Board print
def boardRepresentation():
    board = [[1,2,3],[4,5,6],[7,8,9]]
    for row in board:
        print(' | '.join(map(str,row)))



# Function to print Board
def displayBoard(board):
    for element in board:
        print(' | '.join(map(str,element)))

def playerinput(board,index,mark):

    match

    if board[num] == '-':
        board[num] = mark
        return True
    else:
        print("this position is already Marked, Please Choose another position")
        return False


def isBoardFull(board):
    for element in board:
        if element == '-':
            return False

    return True


def StartGame(board):
    print("This is the initial Board. At you turn Just give the number as input where you want to mark. Player1 - X, Player2 - O")
    boardRepresentation()

    if isBoardFull != True:
        for i in range(1,9):
            if i%2!=0:
                print("Player1 Turn")
                num = int(input())
                playerinput(board,num,'X')
                displayBoard(board)
            else:
                print("Player2 Turn")
                num = int(input())
                playerinput(board,num,'O')
                displayBoard(board)
                



board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]




StartGame(board)
