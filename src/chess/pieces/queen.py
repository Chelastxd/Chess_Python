from piece import *
from chessboard import *

class Queen(Piece):
    def legal_moves(self):
        return self.get_paths(straight=True, diagonal=True)
    
    # Yes, this is the entire Queen function.