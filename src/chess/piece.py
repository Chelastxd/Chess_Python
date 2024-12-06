

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