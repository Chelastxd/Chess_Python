from piece import *
from chessboard import *

class Bishop:
    def legal_moves(self):
        return self.get_paths(diagonal=True)
    
    def is_legal_move(self, new_position):
        return new_position in self.legal_moves() # move to pieces in  the future