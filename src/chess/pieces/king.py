from piece import *
from chessboard import *
from pieces.rook import Rook

class King(Piece):
    def __init__(self, position, color, chessboard):
        super().__init__(position, color, chessboard)
        # super() is used because King.__init__ overwrites Piece.__init__
        self.left_castle = False
        self.right_castle = False

    def legal_moves(self):
        self.left_castle = False
        self.right_castle = False

        short_path = []
        legal_moves_list = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                short_path.append((self.position[0]+i, self.position[1]+j))

        for piece in self.chessboard.piecelist:
            try:
                if not piece.has_moved:
                    good_castle = True
                    if piece.position == (0,0):
                        for i in [1, 2 ,3]: # left space between rook and king
                            if self.chessboard.get_piece(i, 7*self.color) != None:
                                good_castle = False
                        for i in [2 ,3]:
                            if self.position_is_attacked(i, 7*self.color):
                                good_castle = False
                        if good_castle:
                            legal_moves_list.append((2, 0))
                            self.left_castle = True

                    elif piece.position == (7,0):
                        for i in [5, 6]: # right space between rook and king
                            if self.chessboard.get_piece(i, 7*self.color) != None:
                                good_castle = False
                            if self.position_is_attacked(i, 7*self.color):
                                good_castle = False
                        if good_castle:
                            legal_moves_list.append((6, 0))
                            self.right_castle = True
            except: pass # python moment

        for i in short_path:
            if i in self.get_paths(straight=True, diagonal=True) and not self.position_is_attacked(i):
                legal_moves_list.append(i)
        return legal_moves_list
    
    def position_is_attacked(self, position):
        # Returns True if any piece has a legal move that == position.
        for piece in self.chessboard.piecelist:
            if not isinstance(piece, King) and position in piece.legal_moves():
                return True
        return False
    
    def move(self, new_position):
        # REPLACES move() FROM PIECES BECAUSE OF CASTLING !!!
        if self.is_legal_move(new_position):
            if self.chessboard.get_piece(new_position) != None:
                self.chessboard.remove_piece(new_position)
            
            if self.position[0] - new_position[0] == 2 and self.left_castle:
                self.chessboard.move_piece((0, 7*self.color),(3, 7*self.color))

            elif self.position[0] - new_position[0] == -2 and self.right_castle:
                self.chessboard.move_piece((7, 7*self.color),(5, 7*self.color))
                
            self.position = new_position

            

            if self.chessboard.win_condition():
                if self.color:
                    print("RED wins")
                else:
                    print("BLUE wins")
                self.chessboard.finished = True
        else:
            print("Illegal move!")