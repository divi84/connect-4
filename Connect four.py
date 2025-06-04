import random

print("Welcome to connect Four")
print("-----------------------")

possibleLetters = ["A","B","C","D","E","F","G"]
gameBoard=[["","","","","",""],
["","","","","",""],
["","","","","",""],
["","","","","",""],
["","","","","",""],
["","","","","",""]]
rows = 6
cols = 7
def printGameBoard():
    print("\n    A    B    C    D    E    F    G    ", end = " ")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+")
        print(x, "  |",end = "")
        for y in range(cols):
            if(gameBoard[x][y] =="🔴"):
                print("", gameBoard[x][y], end = " |")
            elif(gameBoard[x][y] == "🔵"):
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
                print("\n    +----+----+----+----+----+----+")
                def modifyTurn(spacePicked,turn):
                    gameBoard[spacePicked[0]][spacePicked[1]] = turn
                    
                    turnCounter = 0 
                turnCounter = 0
                while True:
                     printGameBoard()
                     currentPlayer = "Player 1" if turnCounter % 2 == 0 else "Player 2"
                     currentPiece = "🔴" if turnCounter % 2 == 0 else "🔵"
    
                     move = input(f"{currentPlayer} ({currentPiece}), choose a column (A-G): ").strip().upper()
    
                     if move not in possibleLetters:
                      print("Invalid input. Please choose a letter from A to G.")
                     continue
    
                     columnIndex = possibleLetters.index(move)
    
                     if not drop_piece(columnIndex, currentPiece):
                      print("Column is full. Try a different one.")
                     continue
                     turnCounter += 1
