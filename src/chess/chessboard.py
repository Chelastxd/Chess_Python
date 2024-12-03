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
        return None
    
    def board_display(self):
        display = {}
        for rank in range(8):
            display[rank] = {}
            for file in range(8):

                display[rank][file] = " "
                for piece in self.piecelist:
                    if (file, rank) == piece.position:
                        display[rank][file] = str(0 + piece.color) # temporary black/white pawn display, True as "1"

        for i in range(8):
            print(list(display[7-i].values())) # top to bottom display using 8 print commands