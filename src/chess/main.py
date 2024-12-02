from chessboard import *
from piece import *
from pawn import *


chessboard = Chessboard()

for i in range(1,8):
    chessboard.add_piece(Pawn((i,2),True,chessboard))
    chessboard.add_piece(Pawn((i,7),False,chessboard))

#print(chessboard.piecelist)