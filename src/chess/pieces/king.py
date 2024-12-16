from piece import *
from chessboard import *

class King:
    def legal_moves(self):
        legal_moves_list = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                short_path = [self.position[0]+i, self.position[1]+j]

        for i in self.get_paths(straight=True, diagonal=True):
            if i in short_path and self.position_is_attacked(i) == False:
                legal_moves_list.append(i)
        return legal_moves_list
    
    def position_is_attacked(self, position):
        # Returns True if any piece has a legal move that == position.
        for piece in self.chessboard.piecelist:
            if position in piece.legal_moves():
                return True
        return False