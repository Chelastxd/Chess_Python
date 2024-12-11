

class Piece:
    def __init__(self, position, color, chessboard):
        self.position = position #tupel
        self.color = color #boolean (white is True)
        self.chessboard = chessboard

    def is_legal_move(self, neue_position):
        print("Error1")

    def legal_moves(self, new_pos):
        print("Error1b")

    def move(self, new_position):
        if self.is_legal_move(new_position)[0]:
            if self.is_legal_move(new_position)[1]:
                self.chessboard.remove_piece(new_position)
            self.position = new_position
            if self.chessboard.win_condition():
                if self.color:
                    print("RED wins")
                else:
                    print("BLUE wins")
                self.chessboard.finished = True
        else:
            print("Illegal move!")

    def get_paths(self, diagonal=False, straight=False):
        legal_moves_list = []
        if straight:
            for i in range(0, -self.position[1] + 7): # up
                if i != 0:
                    pos = (self.position[0], i)
                    piece_found = pos in [j.position for j in self.chessboard.piecelist]
                    if not piece_found:
                        legal_moves_list.append(pos)
                    elif piece_found and self.chessboard.get_piece(pos).color != self.color:
                        legal_moves_list.append(pos)
                    else:
                        break
            for i in range(-self.position[1], 0): # down
                if i != 0:
                    pos = (self.position[0], -i)
                    piece_found = pos in [j.position for j in self.chessboard.piecelist]
                    if not piece_found:
                        legal_moves_list.append(pos)
                    elif piece_found and self.chessboard.get_piece(pos).color != self.color:
                        legal_moves_list.append(pos)
                    else:
                        break
            for i in range(-self.position[0], 0): # left
                if i != 0:
                    pos = (-i, self.position[1])
                    piece_found = pos in [j.position for j in self.chessboard.piecelist]
                    if not piece_found:
                        legal_moves_list.append(pos)
                    elif piece_found and self.chessboard.get_piece(pos).color != self.color:
                        legal_moves_list.append(pos)
                    else:
                        break
            for i in range(0, -self.position[0] + 7): # right
                if i != 0:
                    pos = (i, self.position[1])
                    piece_found = pos in [j.position for j in self.chessboard.piecelist]
                    if not piece_found:
                        legal_moves_list.append(pos)
                    elif piece_found and self.chessboard.get_piece(pos).color != self.color:
                        legal_moves_list.append(pos)
                    else:
                        break
        return legal_moves_list