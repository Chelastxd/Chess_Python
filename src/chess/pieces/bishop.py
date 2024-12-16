from piece import *
from chessboard import *

class Bishop:
    def legal_moves(self):
        return self.get_paths(diagonal=True)
    
    # Yes, this is the entire Bishop function.