from piece import *
from chessboard import *

class King:
    def legal_moves(self):
        legal_moves_list = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                short_path = [self.position[0]+i, self.position[1]+j]

        for i in self.get_paths(straight=True, diagonal=True):
            if i in short_path:
                legal_moves_list.append(i)

        return legal_moves_list
    
    def is_legal_move(self, new_position):
        return new_position in self.legal_moves() # move to pieces in the future
    
    def position_is_attacked(position):
        for piece in self.chessboard.piecelist:
            pass # check all pieces if they attack here