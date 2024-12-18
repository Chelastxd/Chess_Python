from piece import *
from chessboard import *
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight



class Pawn(Piece):
    def legal_moves(self):
        legal_moves_list = []
        short_moves = [(self.position[0], self.position[1] + (2*self.color - 1))]
        short_moves.append((self.position[0], self.position[1] + (4*self.color - 2)))
        short_captures = [(self.position[0]-1, self.position[1] + (2*self.color - 1))]
        short_captures.append((self.position[0]+1, self.position[1] + (2*self.color - 1)))

        for i in self.get_paths(straight=True):
            if i in short_moves:
                legal_moves_list.append(i)

        for i in short_captures:
            if self.chessboard.get_piece(i) != None and self.chessboard.get_piece(i) in self.get_paths(diagonal=True):
                legal_moves_list.append(i)

        return legal_moves_list
    
    def promotion(self):
        if self.position[1] == (7*self.color):
            self.chessboard.remove_piece(self.position)
            completed = False
            while not completed:
                new_piece = input("What would you like to promote to?")
                if new_piece.lower() == "queen":
                    self.chessboard.add_piece(Queen,self.color,self.position)
                    completed = True
                elif new_piece.lower() == "rook":
                    self.chessboard.add_piece(Rook,self.color,self.position)
                    completed = True
                elif new_piece.lower() == "bishop":
                    self.chessboard.add_piece(Bishop,self.color,self.position)
                    completed = True
                elif new_piece.lower() == "knight":
                    self.chessboard.add_piece(Knight,self.color,self.position)
                    completed = True
                else:
                    print("invalid piece name, you can promote to 'Queen', 'Rook', 'Bishop' or 'Knight'")
                    
#-- Redundant/old code --------------------------------------------------------#

# class Pawn(Piece):
#     def legal_moves(self, new_position):
#         legal_moves = []
#         legal_captures = []
#         piece_new_position = self.chessboard.get_piece(new_position)

#         if self.color == True: # white
#             if piece_new_position == None and (self.position[0], self.position[1] + 1) == new_position:
#                 legal_moves.append((self.position,new_position))

#             elif piece_new_position != None and piece_new_position.color != self.color:
#                 if (self.position[0] - 1, self.position[1] + 1) == piece_new_position.position or (self.position[0] + 1, self.position[1] + 1) == piece_new_position.position:
#                     legal_captures.append((self.position,new_position))

#         elif self.color == False: # black
#             if piece_new_position == None and (self.position[0], self.position[1] - 1) == new_position:
#                 legal_moves.append((self.position,new_position))

#             elif piece_new_position != None and piece_new_position.color != self.color:
#                 if (self.position[0] - 1, self.position[1] - 1) == piece_new_position.position or (self.position[0] + 1, self.position[1] - 1) == piece_new_position.position:
#                     legal_captures.append((self.position,new_position))
#         return legal_moves, legal_captures

#     def is_legal_move(self, new_position):
#         if self.legal_moves(new_position) is not None:
#             for move in self.legal_moves(new_position)[0]:
#                 if move == (self.position, new_position):
#                     return True, False
                
#             for move in self.legal_moves(new_position)[1]:
#                 if move == (self.position, new_position):
#                     return True, True
#             return False, False