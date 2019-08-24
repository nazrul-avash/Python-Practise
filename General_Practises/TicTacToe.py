#Tic-Tac-Toe Game
def printBoard(board):
    print(board["tL"]+ "|" + board["tM"]+ "|" + board["tR"] )
    print("-+-+-")
    print(board["mL"]+ "|" + board["mM"]+ "|" + board["mR"] )
    print("-+-+-")
    print(board["lL"]+ "|" + board["lM"]+ "|" + board["lR"] )
board = {"tL":" ","tM":" ","tR":" ","mL":" ", "mM":" ", "mR":" ", "lL":" ", "lM":" ", "lR":" "}
turn = "x"
for i in range(9):
    printBoard(board)
    print("Where do you like to put it, Mr./Mrs." + turn+"?")
    slot = input()
    board[slot] = turn
    if turn == "x":
        turn = "o"
    else:
        turn = "x"
printBoard(board)
