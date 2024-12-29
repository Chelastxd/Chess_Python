from piece import *
from chessboard import *

class Knight(Piece):
    def legal_moves(self):
        legal_moves_list = []
        short_path = []
        for i in [-2, 2]:
            for j in [-1, 1]:
                short_path.append((self.position[0]+i, self.position[1]+j))
                short_path.append((self.position[0]+j, self.position[1]+i))

        for position in short_path:
            if 0 <= position[0] <= 7 and 0 <= position[1] <= 7:
                if self.chessboard.get_piece(position) == None or self.chessboard.get_piece(position).color != self.color:
                    legal_moves_list.append(position)

        return legal_moves_list

        