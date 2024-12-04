from piece import *

class Chessboard():
    def __init__(self):
        self.piecelist = []

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
    
    def board_display(self):
        display = {}
        for rank in range(8):
            display[rank] = {}
            for file in range(8):

                display[rank][file] = " "
                for piece in self.piecelist:
                    if (file, rank) == piece.position:
                        display[rank][file] = str(0 + piece.color) # temporary black/white pawn display, True as "1"

        for i in range(8):
            print(list(display[7-i].values())) # top to bottom display using 8 print commands

    def piece_dictionary(self):
        piece_dic = {}
        for piece in self.piecelist:
            piece_dic[piece.position] = piece
        return piece_dic

    def board_status(self):
        piece_dic = self.piece_dictionary()
        board_dic = {}
        for j in range(8):
            board_dic[j] = []
            for i in range(8):
                piece = piece_dic.get((i,j))
                if piece != None:
                    board_dic[j].append("P")
                else:
                    board_dic[j].append("X")
            print(board_dic[j])

    def win_condition(self):
        for piece in self.piecelist:
            for i in range(8):
                if piece.self_color == True and piece.position == (i, 7):
                    print("White wins!")
                elif piece.self_color == False and piece.position == (i, 0):
                    print("Black wins!")

