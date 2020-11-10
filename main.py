from Pieces import *

def zadanie2(checkboard):
    arrOfPieces = []
    kings = []

    for i in range(8):
        for j in range(8):
            if checkboard[i][j][0] == 'b':
                clr = 'Czarny'
            elif checkboard[i][j][0] == 'w':
                clr = 'Biały'
            if checkboard[i][j][1] == 'W':
                k = King(i, j, clr)
                arrOfPieces.append(k)
                kings.append(k)
            elif checkboard[i][j][1] == 'q':
                arrOfPieces.append(Queen(i, j, clr))
            elif checkboard[i][j][1] == 'r':
                arrOfPieces.append(Rook(i, j, clr))
            elif checkboard[i][j][1] == 'b':
                arrOfPieces.append(Bishop(i, j, clr))
            elif checkboard[i][j][1] == 'k':
                arrOfPieces.append(Knight(i, j, clr))
            elif checkboard[i][j][1] == 'p':
                arrOfPieces.append(Pawn(i, j, clr))

    # Sprawdzamy czy pozycja nie jest nienormalna
    for king in kings:
        if king.checkIfUnderCheck(arrOfPieces):
            if kings.index(king) == 0:
                if kings[1].checkIfUnderCheck(arrOfPieces):
                    return "Dana pozycja nie może być zinterpretowana poprawnie"
            elif kings.index(king) == 1:
                if kings[0].checkIfUnderCheck(arrOfPieces):
                    return "Dana pozycja nie może być zinterpretowana poprawnie"
            else:
                if king.color == "Biały":
                    return "Czarny wygrał"
                else:
                    return "Biały wygrał"

    set_controlledTilesForAll(arrOfPieces)
    set_movement_for_all(arrOfPieces)

    for piece in arrOfPieces:

        for move in piece.possibleMoves:
            if (piece.name == "Pawn" and piece.color == "Biały" and move[0] == 0) or (piece.name == "Pawn" and piece.color == "Czarny" and move[0] == 7):
                # Królowa
                previous_row = piece.row
                previous_column = piece.column
                piece.row = -1
                piece.column = -1
                arrOfPieces.append(Queen(move[0], move[1], piece.color))
                set_controlledTilesForAll(arrOfPieces)
                piece.controlledTiles.clear()
                revive_piece = False

                for piece2 in arrOfPieces:
                    if piece2.row == arrOfPieces[-1].row and piece2.column == arrOfPieces[-1].column and piece2.color != arrOfPieces[-1].color:
                        piece2.controlledTiles.clear()
                        piece2.row = -1
                        piece2.row = -1
                        revive_piece = True
                        ind = arrOfPieces.index(piece2)
                for king in kings:
                    if king.color == arrOfPieces[-1].color and not king.checkIfUnderCheck(arrOfPieces):
                        set_movement_for_all()
                        if kings.index(king) == 0:
                            if kings[1].checkIfUnderCheckmate(arrOfPieces):
                                return arrOfPieces[-1].color + " może wygrać" + field_interpreter(
                                    (previous_row, previous_column)) + field_interpreter((arrOfPieces[-1].row, arrOfPieces[-1].column)) + "Q"
                        elif kings.index(king) == 1:
                            if kings[0].checkIfUnderCheckmate(arrOfPieces):
                                return piece.color + " może wygrać" + field_interpreter(
                                    (previous_row, previous_column)) + field_interpreter((arrOfPieces[-1].row, arrOfPieces[-1].column)) + "Q"
                if revive_piece:
                    arrOfPieces[ind].row = piece.row
                    arrOfPieces[ind].column = piece.column
                piece.row = previous_row
                piece.column = previous_column
                arrOfPieces.pop()






                #Wieża
                previous_row = piece.row
                previous_column = piece.column
                piece.row = -1
                piece.column = -1
                arrOfPieces.append(Rook(move[0], move[1], piece.color))
                set_controlledTilesForAll(arrOfPieces)
                piece.controlledTiles.clear()
                revive_piece = False

                for piece2 in arrOfPieces:
                    if piece2.row == arrOfPieces[-1].row and piece2.column == arrOfPieces[-1].column and piece2.color != arrOfPieces[-1].color:
                        piece2.controlledTiles.clear()
                        piece2.row = -1
                        piece2.row = -1
                        revive_piece = True
                        ind = arrOfPieces.index(piece2)
                for king in kings:
                    if king.color == arrOfPieces[-1].color and not king.checkIfUnderCheck(arrOfPieces):
                        set_movement_for_all()
                        if kings.index(king) == 0:
                            if kings[1].checkIfUnderCheckmate(arrOfPieces):
                                return arrOfPieces[-1].color + " może wygrać" + field_interpreter(
                                    (previous_row, previous_column)) + field_interpreter(
                                    (arrOfPieces[-1].row, arrOfPieces[-1].column)) + "R"
                        elif kings.index(king) == 1:
                            if kings[0].checkIfUnderCheckmate(arrOfPieces):
                                return piece.color + " może wygrać" + field_interpreter(
                                    (previous_row, previous_column)) + field_interpreter(
                                    (arrOfPieces[-1].row, arrOfPieces[-1].column)) + "R"
                if revive_piece:
                    arrOfPieces[ind].row = piece.row
                    arrOfPieces[ind].column = piece.column
                piece.row = previous_row
                piece.column = previous_column
                arrOfPieces.pop()








                # Goniec
                previous_row = piece.row
                previous_column = piece.column
                piece.row = -1
                piece.column = -1
                arrOfPieces.append(Bishop(move[0], move[1], piece.color))
                set_controlledTilesForAll(arrOfPieces)
                piece.controlledTiles.clear()
                revive_piece = False

                for piece2 in arrOfPieces:
                    if piece2.row == arrOfPieces[-1].row and piece2.column == arrOfPieces[-1].column and piece2.color != arrOfPieces[-1].color:
                        piece2.controlledTiles.clear()
                        piece2.row = -1
                        piece2.row = -1
                        revive_piece = True
                        ind = arrOfPieces.index(piece2)
                for king in kings:
                    if king.color == arrOfPieces[-1].color and not king.checkIfUnderCheck(arrOfPieces):
                        set_movement_for_all()
                        if kings.index(king) == 0:
                            if kings[1].checkIfUnderCheckmate(arrOfPieces):
                                return arrOfPieces[-1].color + " może wygrać" + field_interpreter(
                                    (previous_row, previous_column)) + field_interpreter(
                                    (arrOfPieces[-1].row, arrOfPieces[-1].column)) + "B"
                        elif kings.index(king) == 1:
                            if kings[0].checkIfUnderCheckmate(arrOfPieces):
                                return piece.color + " może wygrać" + field_interpreter(
                                    (previous_row, previous_column)) + field_interpreter(
                                    (arrOfPieces[-1].row, arrOfPieces[-1].column)) + "B"
                if revive_piece:
                    arrOfPieces[ind].row = piece.row
                    arrOfPieces[ind].column = piece.column
                piece.row = previous_row
                piece.column = previous_column
                arrOfPieces.pop()






                # Koń
                previous_row = piece.row
                previous_column = piece.column
                piece.row = -1
                piece.column = -1
                arrOfPieces.append(Knight(move[0], move[1], piece.color))
                set_controlledTilesForAll(arrOfPieces)
                piece.controlledTiles.clear()
                revive_piece = False

                for piece2 in arrOfPieces:
                    if piece2.row == arrOfPieces[-1].row and piece2.column == arrOfPieces[-1].column and piece2.color != \
                            arrOfPieces[-1].color:
                        piece2.controlledTiles.clear()
                        piece2.row = -1
                        piece2.row = -1
                        revive_piece = True
                        ind = arrOfPieces.index(piece2)
                for king in kings:
                    if king.color == arrOfPieces[-1].color and not king.checkIfUnderCheck(arrOfPieces):
                        set_movement_for_all()
                        if kings.index(king) == 0:
                            if kings[1].checkIfUnderCheckmate(arrOfPieces):
                                return arrOfPieces[-1].color + " może wygrać" + field_interpreter(
                                    (previous_row, previous_column)) + field_interpreter(
                                    (arrOfPieces[-1].row, arrOfPieces[-1].column)) + "K"
                        elif kings.index(king) == 1:
                            if kings[0].checkIfUnderCheckmate(arrOfPieces):
                                return piece.color + " może wygrać" + field_interpreter(
                                    (previous_row, previous_column)) + field_interpreter(
                                    (arrOfPieces[-1].row, arrOfPieces[-1].column)) + "K"
                if revive_piece:
                    arrOfPieces[ind].row = piece.row
                    arrOfPieces[ind].column = piece.column
                piece.row = previous_row
                piece.column = previous_column
                arrOfPieces.pop()

            else:

                previous_row = piece.row
                previous_column = piece.column
                piece.row = move[0]
                piece.column = move[1]
                set_controlledTilesForAll(arrOfPieces)
                revive_piece = False

                for piece2 in arrOfPieces:
                    if piece2.row == piece.row and piece2.column == piece.column and piece2.color != piece.color:
                        piece2.controlledTiles.clear()
                        piece2.row = -1
                        piece2.row = -1
                        revive_piece = True
                        ind = arrOfPieces.index(piece2)
                for king in kings:
                    if king.color == piece.color and not king.checkIfUnderCheck(arrOfPieces):
                        set_movement_for_all()
                        if kings.index(king) == 0:
                            if kings[1].checkIfUnderCheckmate(arrOfPieces):
                                return piece.color + " może wygrać" + field_interpreter((previous_row, previous_column)) + field_interpreter((piece.row, piece.column))
                        elif kings.index(king) == 1:
                            if kings[0].checkIfUnderCheckmate(arrOfPieces):
                                return piece.color + " może wygrać" + field_interpreter((previous_row, previous_column)) + field_interpreter((piece.row, piece.column))
                if revive_piece:
                    arrOfPieces[ind].row = piece.row
                    arrOfPieces[ind].column = piece.column
                piece.row = previous_row
                piece.column = previous_column

    return "Żadna strona nie jest w stanie wygrać w jednym ruchu"
