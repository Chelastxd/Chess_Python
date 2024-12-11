from chessboard import *
from piece import *
from pawn import *
from utils import *
from inputparser import *

chessboard = Chessboard()

for i in range(8): # 0-7
    chessboard.add_piece(Pawn((i,1),True,chessboard))
    chessboard.add_piece(Pawn((i,6),False,chessboard))

print()
print("\x1b[31mRed's Turn\x1b[0m")
chessboard.board_status()
# main loop
while True:
    if chessboard.finished:
        break
    player_move = translate(input("Select and move piece. // Example: 'a2 to a3': ")) # Hauptsache die ersten und letzten beiden Zeichen stimmen!
    if player_move == None:
        print("Incorrect syntax")
        continue
    error = chessboard.move_piece(player_move[0],player_move[1])
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

print("RESET FILE FOR NEW GAME!")