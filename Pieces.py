#Tu znajdują się klasy wszystkich figur

class King(object):
    def __init__(self, row, column, color):
        self.name = "King"
        self.color = color
        self.row = row
        self.column = column
        self.controlledTiles = []
        self.possibleMoves = []

    def checkIfUnderCheck(self, arrOfPieces):
        for i in arrOfPieces:
            if (self.row, self.column) in i.controlledTiles and i.color != self.color:
                return True
        return False

    def checkIfUnderCheckmate(self, arrOfPieces):
        for i in arrOfPieces:
            if (self.row, self.column) in i.controlledTiles and i.color != self.color and len(self.possibleMoves) == 0:
                for j in arrOfPieces:
                    if (i.row, i.column) in j.controlledTiles and j.color == self.color and j.name != "King":
                        return False
                if i.name == "Knight" or i.name == "Pawn":
                    return True
                if self.row == i.row:
                    if self.column < i.column:
                        for k in arrOfPieces:
                            if k.color == self.color:
                                for z in k.controlledTiles:
                                    if z[0] == self.row and self.column < z[1] < i.column:
                                        return False
                    else:
                        for k in arrOfPieces:
                            if k.color == self.color:
                                for z in k.controlledTiles:
                                    if z[0] == self.row and i.column < z[1] < self.column:
                                        return False
                elif self.column == self.column:
                    if self.row < i.row:
                        for k in arrOfPieces:
                            if k.color == self.color:
                                for z in k.controlledTiles:
                                    if z[1] == self.column and self.row < z[0] < i.row:
                                        return False
                    else:
                        for k in arrOfPieces:
                            if k.color == self.color:
                                for z in k.controlledTiles:
                                    if z[1] == self.column and i.row < z[0] < self.row:
                                        return False
                else:
                    y = i.row
                    x = i.column
                    if self.row < i.row:
                        if self.column < i.column:
                            while y > self.row and x > self.column:
                                for k in arrOfPieces:
                                    if k.color == self.color and (y, x) in k.controlledTiles:
                                        return False
                                x -= 1
                                y -= 1
                        else:
                            while y > self.row and x < self.column:
                                for k in arrOfPieces:
                                    if k.color == self.color and (y, x) in k.controlledTiles:
                                        return False
                                x += 1
                                y -= 1
                    else:
                        if self.column < i.column:
                            while y < self.row and x > self.column:
                                for k in arrOfPieces:
                                    if k.color == self.color and (y, x) in k.controlledTiles:
                                        return False
                                x -= 1
                                y += 1
                        else:
                            while y < self.row and x < self.column:
                                for k in arrOfPieces:
                                    if k.color == self.color and (y, x) in k.controlledTiles:
                                        return False
                                x += 1
                                y += 1
                return True
        return False

    def set_controlledTiles(self, arrOfPieces):
        for i in range(self.row - 1, self.row + 2):
            for j in range(self.column - 1, self.column + 2):
                if 7 >= i >= 0 and 7 >= j >= 0 and i != self.row and j != self.column:
                    self.controlledTiles.append((i, j))

    def set_movement(self, arrOfPieces):
        for i in self.controlledTiles:
            for j in arrOfPieces:
                if (j.row, j.column) == i:
                    if j.color != self.color:
                        boolean = True
                        for k in arrOfPieces:
                            if i in k.controlledTiles and k.color != self.color:
                                boolean = False
                        if boolean:
                            self.possibleMoves.append(i)
                else:
                    self.possibleMoves.append(i)


class Queen(object):
    def __init__(self, row, column, color):
        self.name = "Queen"
        self.color = color
        self.row = row
        self.column = column
        self.controlledTiles = []
        self.possibleMoves = []

    def set_controlledTiles(self, arrOfPieces):
        set_FilesOrDiagonals(self, arrOfPieces, self.row - 1, self.column - 1, -1, -1)
        set_FilesOrDiagonals(self, arrOfPieces, self.row + 1, self.column + 1, +1, +1)
        set_FilesOrDiagonals(self, arrOfPieces, self.row + 1, self.column - 1, +1, -1)
        set_FilesOrDiagonals(self, arrOfPieces, self.row - 1, self.column + 1, -1, +1)
        set_FilesOrDiagonals(self, arrOfPieces, self.row - 1, self.column, -1, 0)
        set_FilesOrDiagonals(self, arrOfPieces, self.row + 1, self.column, 1, 0)
        set_FilesOrDiagonals(self, arrOfPieces, self.row, self.column - 1, 0, -1)
        set_FilesOrDiagonals(self, arrOfPieces, self.row, self.column + 1, 0, 1)

    def set_movement(self, arrOfPieces):
        set_movement(self, arrOfPieces)

class Rook(object):
    def __init__(self, row, column, color):
        self.name = "Rook"
        self.color = color
        self.row = row
        self.column = column
        self.controlledTiles = []
        self.possibleMoves = []

    def set_controlledTiles(self, arrOfPieces):
        set_FilesOrDiagonals(self, arrOfPieces, self.row - 1, self.column, -1, 0)
        set_FilesOrDiagonals(self, arrOfPieces, self.row + 1, self.column, 1, 0)
        set_FilesOrDiagonals(self, arrOfPieces, self.row, self.column - 1, 0, -1)
        set_FilesOrDiagonals(self, arrOfPieces, self.row, self.column + 1, 0, 1)

    def set_movement(self, arrOfPieces):
        set_movement(self, arrOfPieces)


class Bishop(object):
    def __init__(self, row, column, color):
        self.name = "Bishop"
        self.color = color
        self.row = row
        self.column = column
        self.controlledTiles = []
        self.possibleMoves = []

    def set_controlledTiles(self, arrOfPieces):
        set_FilesOrDiagonals(self, arrOfPieces, self.row - 1, self.column - 1, -1, -1)
        set_FilesOrDiagonals(self, arrOfPieces, self.row + 1, self.column + 1, 1, 1)
        set_FilesOrDiagonals(self, arrOfPieces, self.row + 1, self.column - 1, 1, -1)
        set_FilesOrDiagonals(self, arrOfPieces, self.row - 1, self.column + 1, -1, 1)


    def set_movement(self, arrOfPieces):
        set_movement(self, arrOfPieces)


class Knight(object):
    def __init__(self, row, column, color):
        self.name = "Knight"
        self.color = color
        self.row = row
        self.column = column
        self.controlledTiles = []
        self.possibleMoves = []
        self.allpossible = [(row+1, column+2), (row-1, column+2), (row+1, column-2), (row-1, column-2), (row+2, column+1), (row-2, column+1), (row+2, column-1), (row-2, column-1)]

    def set_controlledTiles(self, arrOfPieces):
        for i in self.allpossible:
            if 0 < i[0] < 7 or 0 < i[1] < 7:
                self.controlledTiles.append(i)

    def set_movement(self, arrOfPieces):
        set_movement(self, arrOfPieces)

class Pawn(object):
    def __init__(self, row, column, color):
        self.name = "Pawn"
        self.color = color
        self.row = row
        self.column = column
        self.controlledTiles = []
        self.possibleMoves = []

    def set_controlledTiles(self, arrOfPieces):
        if self.color == "Biały":
            if self.column == 0:
                self.controlledTiles.append((self.row - 1, self.column + 1))
            elif self.column == 7:
                self.controlledTiles.append((self.row - 1, self.column - 1))
            else:
                self.controlledTiles.append((self.row - 1, self.column + 1))
                self.controlledTiles.append((self.row - 1, self.column - 1))

        if self.color == "Czarny":
            if self.column == 0:
                self.controlledTiles.append((self.row + 1, self.column + 1))
            elif self.column == 7:
                self.controlledTiles.append((self.row + 1, self.column - 1))
            else:
                self.controlledTiles.append((self.row + 1, self.column + 1))
                self.controlledTiles.append((self.row + 1, self.column - 1))

    def set_movement(self, arrOfPieces):
        if self.color == "Czarny":
            if self.row == 6:
                if not (self.row - 1, self.column) in arrOfPieces.values():
                    self.possibleMoves.append((self.row - 1, self.column))
                if not (self.row - 2, self.column) in arrOfPieces.values():
                    self.possibleMoves.append((self.row - 2, self.column))
            else:
                if not (self.row - 1, self.column) in arrOfPieces.values():
                    self.possibleMoves.append((self.row - 1, self.column))
            for i in self.controlledTiles:
                for j in arrOfPieces:
                    if i == (j.row, j.column) and j.color == "Czarny":
                        self.possibleMoves.append(i)

        else:
            if self.row == 1:
                if not (self.row + 1, self.column) in arrOfPieces.values():
                    self.possibleMoves.append((self.row + 1, self.column))
                if not (self.row + 2, self.column) in arrOfPieces.values():
                    self.possibleMoves.append((self.row + 2, self.column))
            else:
                if not (self.row + 1, self.column) in arrOfPieces.values():
                    self.possibleMoves.append((self.row + 1, self.column))
            for i in self.controlledTiles:
                for j in arrOfPieces:
                    if i == (j.row, j.column) and j.color == "Biały":
                        self.possibleMoves.append(i)






def set_FilesOrDiagonals(obj, arrOfPieces, i, j, incr_i, incr_j):
    boolean = True
    while 0 <= i <= 7 and 0 <= j <= 7 and boolean:
        for k in arrOfPieces:
            if (i, j) == (k.row, k.column):
                boolean = False
                break
        obj.controlledTiles.append((i, j))
        i += incr_i
        j += incr_j


def set_controlledTilesForAll(arrOfPieces):
    for i in arrOfPieces:
        i.set_controlledTiles(arrOfPieces)


def set_movement(obj, arrOfPieces):
    for i in obj.controlledTiles:
        for j in arrOfPieces:
            if (j.row, j.column) == i:
                if j.color != obj.color:
                    obj.possibleMoves.append(i)
            else:
                obj.possibleMoves.append(i)
def set_movement_for_all(arrOfPieces):
    for i in arrOfPieces:
        i.set_movement(arrOfPieces)

def field_interpreter(field):
    pole = ''
    if field[1] == 0:
        pole += 'a'
    if field[1] == 1:
        pole += 'b'
    if field[1] == 2:
        pole += 'c'
    if field[1] == 3:
        pole += 'd'
    if field[1] == 4:
        pole += 'e'
    if field[1] == 5:
        pole += 'f'
    if field[1] == 6:
        pole += 'g'
    if field[1] == 7:
        pole += 'h'
    pole += (8 - field[0])
    return pole
