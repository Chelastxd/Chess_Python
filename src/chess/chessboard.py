from piece import *
from utils import *

class Chessboard():
    def __init__(self):
        self.piecelist = []
        self.finished = False

    def move_piece(self, position, new_position):
        for piece in self.piecelist:
            if piece.position == position and piece.is_legal_move(new_position):
                self.get_piece(position).move(new_position)
            if self.win_condition():
                if piece.color:
                    print("White wins!!!")
                else:
                    print("Black wins!!!")

    def add_piece(self, piece):
        self.piecelist.append(piece)

    def remove_piece(self, position):
        for piece in self.piecelist:
            if piece.position == position:
                self.piecelist.remove(piece)
    
    def get_piece(self, position):
        for piece in self.piecelist:
            if piece.position == position:
                return piece
        return None
    
    #def board_display(self): # OUTDATED PAWN DISPLAY
        display = {}
        for rank in range(8):
            display[rank] = {}
            for file in range(8):

                display[rank][file] = " "
                for piece in self.piecelist:
                    if (file, rank) == piece.position:
                        display[rank][file] = str(0 + piece.color)

        for i in range(8):
            print(list(display[7-i].values()))

    def piece_dictionary(self):
        piece_dic = {}
        for piece in self.piecelist:
            piece_dic[piece.position] = piece
        return piece_dic

    def board_status(self):
        piece_dic = self.piece_dictionary()
        board_dic = {}
        print()
        for j in range(7, -1, -1): # range(7, -1, -1) statt range(8), damit weiß auch unten ist
            board_dic[j] = []
            for i in range(8):
                piece = piece_dic.get((i,j))
                if piece != None:
                    if piece.color:
                        board_dic[j].append("\x1b[31mP\x1b[0m")
                    else:
                        board_dic[j].append("\x1b[34mP\x1b[0m")
                else:
                    board_dic[j].append("·")
            print("\x1b[90m" + str(j+1) +"\x1b[0m" + "   " + list_to_string(board_dic[j]))
        print("\n    \x1b[90mA  B  C  D  E  F  G  H\x1b[0m \n")

    def win_condition(self):
        for piece in self.piecelist:
            for i in range(8):
                if piece.color == True and piece.position == (i, 7):
                    return True
                elif piece.color == False and piece.position == (i, 0):
                    return True
        return False

