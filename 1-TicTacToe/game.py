def playGame() :
    board = [[1,2,3],[4,5,6],[7,8,9]]
    print("Current is Tic-Tac-Toe Board, Enter the number where you want to mark at your turn. Player 1 will be marked with 'X' and Player 2 will be marked with 'O'")
    printBoard(board)

    print("Game Starting Now")




def printBoard(board):
    for row in board:
        print("|".join(map(str,row)))






playGame()