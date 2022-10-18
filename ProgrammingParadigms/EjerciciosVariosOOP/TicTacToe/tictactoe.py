class Board:

    def __init__(self):
        self.grid = [[0,0,0],[0,0,0],[0,0,0]]
    
    def xmove(self, position):
        self.grid[position[0]][position[1]] = 1

    def omove(self, position):
        self.grid[position[0]][position[1]] = 2

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
            if len(set(row)) == 1 and row[0] != 0:
                return row[0]
        return 0
    
    @staticmethod
    def checkColumns(list):
        return Board.checkRows(Board.tranposeGrid(list))

    def checkBoard(self):
        rowCheck = Board.checkRows(self.grid)
        if rowCheck != 0:
            return Board.checkRows(self.grid)
        columnCheck = Board.checkColumns(self.grid)
        if columnCheck != 0:
            return columnCheck
        return 0
        


    

    