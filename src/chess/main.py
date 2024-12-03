from chessboard import *
from piece import *
from pawn import *


chessboard = Chessboard()

for i in range(8): # 0-7
    chessboard.add_piece(Pawn((i,1),True,chessboard))
    chessboard.add_piece(Pawn((i,6),False,chessboard))


# Testing / proof of concept
chessboard.board_display() # currently just 8 seperate print functions

chessboard.get_piece((0, 1)).move((0, 2))

print("")
chessboard.board_display()