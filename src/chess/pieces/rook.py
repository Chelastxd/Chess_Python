from piece import *
from chessboard import *

class Rook(Piece):
    def __init__(self, position, color, chessboard):
        super().__init__(position, color, chessboard)
        # super() is used because Rook.__init__ overwrites Piece.__init__
        self.has_moved = False
        
    def legal_moves(self):
        return self.get_paths(straight=True)
    
    # Yes, this is the entire Rook function.