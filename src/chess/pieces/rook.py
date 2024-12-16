from piece import *
from chessboard import *

class Rook(Piece):
    def legal_moves(self):
        return self.get_paths(straight=True)
    
    # Yes, this is the entire Rook function.