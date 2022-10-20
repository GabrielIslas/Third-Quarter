class Board:

    def __init__(self):
        self.grid = [["-","-","-"],["-","-","-"],["-","-","-"]]
    
    def move(self, position, symbol):
        if position[0] < 0 or position[0] > 2 or position[1] < 0 or position[1] > 2:
            return False
        if self.grid[position[0]][position[1]] == "-":
            self.grid[position[0]][position[1]] = symbol
            return True
        else:
            return False

    @staticmethod
    def transposeGrid(list):
        transposedGrid = [[],[],[]]
        for index in range(3):
            transposedGrid[index].append(list[0][index])
            transposedGrid[index].append(list[1][index])
            transposedGrid[index].append(list[2][index])
        return transposedGrid

    @staticmethod
    def checkRows(list):
        for row in list:
            if len(set(row)) == 1 and row[0] != "-":
                return row[0]
        return 0
    
    @staticmethod
    def checkColumns(list):
        return Board.checkRows(Board.transposeGrid(list))

    @staticmethod
    def checkDiagonals(list):
        if list[0][0] == list[1][1] and list[1][1] == list[2][2] and list[0][0] != "-":
            return list[0][0]
        if list[0][2] == list[1][1] and list[1][1] == list[2][0] and list[0][2] != "-":
            return list[0][2]
        return 0

    def checkBoardWin(self):
        rowCheck = Board.checkRows(self.grid)
        if rowCheck != 0:
            return rowCheck
        columnCheck = Board.checkColumns(self.grid)
        if columnCheck != 0:
            return columnCheck
        diagonalCheck = Board.checkDiagonals(self.grid)
        if diagonalCheck != 0:
            return diagonalCheck
        return 0

    def checkBoardFull(self):
        for row in self.grid:
            for element in row:
                if element == "-":
                    return False
        return True

    def __str__(self):
        returnString = ""
        for row in self.grid:
            for element in row:
                returnString += str(element)
            returnString += "\n"
        return returnString

        
class Game:

    def __init__(self):
        self.board = Board()
        self.turn = None
    
    def chooseSymbol(self):
        print("Choose symbol for first player: ")
        validChoice = False
        while not validChoice:
            choice = input("Type x or o: ")
            if choice == "x":
                self.turn = "x"
                validChoice = True
            elif choice == "o":
                self.turn = "o"
                validChoice = True
            else:
                print("Not a valid input")

    def changeTurn(self):
        if self.turn == "x":
            self.turn = "o"
        elif self.turn == "o":
            self.turn = "x"
    
    def playerMove(self):
        print(self.board)
        print(f"Player {self.turn} turn")
        validMove = False
        while not validMove:
            row = -1
            column = -1
            validRow = False
            validColumn = False
            while not validRow:
                try:
                    row = int(input("Type which row: "))
                    validRow = True
                except ValueError:
                    print("Type an integer")
            while not validColumn:
                try:
                    column = int(input("Type which column: "))
                    validColumn = True
                except ValueError:
                    print("Type an integer")
            move = (row - 1, column - 1)
            if not self.board.move(move, self.turn):
                print("Not a valid move")
            else:
                validMove = True

    def checkGame(self):
        if self.board.checkBoardWin():
            print(f"Player {self.turn} wins")
            return True
        elif self.board.checkBoardFull():
            print("It's a tie")
            return True
        else:
            self.changeTurn()
            return False


programRunning = True
while programRunning:
    print("TicTacToe")
    print("Press Enter to start new game")
    input("")
    tictactoe = Game()
    tictactoe.chooseSymbol()
    gameEnded = False
    while not gameEnded:
        tictactoe.playerMove()
        if tictactoe.checkGame():
            gameEnded = True
    continueGame = input("Type 1 to play again, anything else to exit: ")
    if continueGame != "1":
        programRunning = False