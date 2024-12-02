from piece import *
from chessboard import *

class Pawn(Piece):
    def legal_moves(self, new_position):
        legal_moves = []
        piece_new_position = self.chessboard.get_piece(new_position)

        if self.color == True: # white
            if piece_new_position == None and (self.position[0], self.position[1] + 1) == new_position:
                legal_moves.append((self.position,new_position))
            elif piece_new_position.color != self.color:
                if (self.position[0] - 1, self.position[1] + 1) == piece_new_position.position or (self.position[0] + 1, self.position[1] + 1) == piece_new_position.position:
                    legal_moves.append((self.position,new_position))

        elif self.color == False: # black
            if piece_new_position == None and (self.position[0], self.position[1] - 1) == new_position:
                legal_moves.append((self.position,new_position))
            elif piece_new_position.color != self.color:
                if (self.position[0] - 1, self.position[1] - 1) == piece_new_position.position or (self.position[0] + 1, self.position[1] - 1) == piece_new_position.position:
                    legal_moves.append((self.position,new_position))
        return legal_moves

    def is_legal_move(self, new_position):
        if self.legal_moves(new_position) is not None:
            for move in self.legal_moves(new_position):
                if move == (self.position, new_position):
                    return True
            return False

#self.position = new_position