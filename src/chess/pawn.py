from piece import *
from chessboard import *

class Pawn(Piece):
    def legal_moves(self, new_position):
        legal_moves = []
        for piece in self.chessboard.piecelist:
            if self.chessboard.get_piece(new_position).color != self.color:
                
                legal_moves.append((self.position,new_position))


#self.position = new_position