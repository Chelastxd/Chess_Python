from piece import *

class Chessboard():
    def __init__(self):
        self.piecelist = []

    def add_piece(self, piece):
        self.piecelist.append(piece)

    def remove_piece(self, position):
        for piece in self.piecelist:
            if piece.position == position:
                self.piecelist.remove(piece)
    
    def get_piece(self, position):
        for piece in self.piecelist:
            if piece.position == position:
                return piece