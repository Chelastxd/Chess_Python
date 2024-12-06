from chessboard import *
from piece import *
from pawn import *
from utils import *
from inputparser import *

chessboard = Chessboard()

for i in range(8): # 0-7
    chessboard.add_piece(Pawn((i,1),True,chessboard))
    chessboard.add_piece(Pawn((i,6),False,chessboard))

chessboard.board_status()
# main loop
while True:
    if chessboard.finished:
        break
    player_move = translate(input("Select and move piece. // Example: 'a2 to a3': ")) # Hauptsache die ersten und letzten beiden Zeichen stimmen!
    if player_move == None:
        print("Incorrect syntax")
    else:
        if chessboard.get_piece(player_move[0]) != None:
            chessboard.get_piece(player_move[0]).move(player_move[1])
            chessboard.board_status()
        else:
            print("No piece on that position!")
print("RESET FILE FOR NEW GAME!")