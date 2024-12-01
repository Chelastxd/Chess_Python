

class Piece:
    def __init__(self, position, color, chessboard):
        self.position = position #tupel
        self.color = color #boolean (white is True)
        self.board = chessboard

    def is_legal_move(self, neue_position):
        print("Error1")