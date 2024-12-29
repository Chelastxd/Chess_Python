from chessboard import *
from piece import *
from utils import *
from inputparser import *

from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King

# CHESSBOARD SETUP
chessboard = Chessboard()

for i in range(8): # 0-7
    chessboard.add_piece(Pawn((i,1),True,chessboard))
    chessboard.add_piece(Pawn((i,6),False,chessboard))

for i in [0, 1]:
    chessboard.add_piece(Rook((0,i*7),not i,chessboard))
    chessboard.add_piece(Knight((1,i*7),not i,chessboard))
    chessboard.add_piece(Bishop((2,i*7),not i,chessboard))
    chessboard.add_piece(Queen((3,i*7),not i,chessboard))
    chessboard.add_piece(King((4,i*7),not i,chessboard))
    chessboard.add_piece(Bishop((5,i*7),not i,chessboard))
    chessboard.add_piece(Knight((6,i*7),not i,chessboard))
    chessboard.add_piece(Rook((7,i*7),not i,chessboard))

print("New game")
print("\x1b[31mRed's Turn\x1b[0m")
chessboard.board_status()

# MAIN LOOP
while True:
    if chessboard.finished:
        break

    player_move = translate(input("Select and move piece. // Example: 'a2 to a3': "))
    if player_move == None:
        print("Incorrect syntax")
        continue

    error = chessboard.move_piece(player_move[0], player_move[1])
    if error == None:
        print()
        chessboard.turnchange()
        if chessboard.turnplayer:
            print("\x1b[31mRed's Turn\x1b[0m")
        else:
            print("\x1b[34mBlue's Turn\x1b[0m")
        print()
        chessboard.board_status()
        continue
    print(error)

print()
print("RESTART FILE FOR NEW GAME!")