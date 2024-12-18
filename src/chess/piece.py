

class Piece:
    def __init__(self, position, color, chessboard):
        self.position = position #tupel
        self.color = color #boolean (white/red is True, black/blue is False)
        self.chessboard = chessboard

    def is_legal_move(self, new_position):
        return new_position in self.legal_moves()

    def legal_moves(self, new_pos): # error catching
        print("Error1b: sub_class of piece seems to lack legal_moves()")

    def move(self, new_position):
        if self.is_legal_move(new_position):
            if self.chessboard.get_piece(new_position) != None:
                self.chessboard.remove_piece(new_position)
            self.position = new_position

            if self.chessboard.win_condition():
                if self.color:
                    print("RED wins")
                else:
                    print("BLUE wins")
                self.chessboard.finished = True
        else:
            print("Illegal move!")

    def get_paths(self, diagonal=False, straight=False):
        legal_moves_list = []

        if straight:
            for i in range(self.position[0]-1, -1, -1): # left
                if self.chessboard.get_piece((i, self.position[1])) == None:
                    legal_moves_list.append((i, self.position[1]))
                elif self.chessboard.get_piece((i, self.position[1])) != self.color:
                    legal_moves_list.append((i, self.position[1]))
                    break
                else:
                    break

            for i in range(self.position[0]+1, 8, 1): # right
                if self.chessboard.get_piece((i, self.position[1])) == None:
                    legal_moves_list.append((i, self.position[1]))
                elif self.chessboard.get_piece((i, self.position[1])) != self.color:
                    legal_moves_list.append((i, self.position[1]))
                    break
                else:
                    break

            for i in range(self.position[1]-1, -1, -1): # down
                if self.chessboard.get_piece((self.position[0], i)) == None:
                    legal_moves_list.append((self.position[0], i))
                elif self.chessboard.get_piece((self.position[0], i)) != self.color:
                    legal_moves_list.append((self.position[0], i))
                    break
                else:
                    break

            for i in range(self.position[1]+1, 8, 1): # up
                if self.chessboard.get_piece((self.position[0], i)) == None:
                    legal_moves_list.append((self.position[0], i))
                elif self.chessboard.get_piece((self.position[0], i)) != self.color:
                    legal_moves_list.append((self.position[0], i))
                    break
                else:
                    break
        

        if diagonal:
            for i in range(1, 9): # down_left
                if self.chessboard.get_piece((self.position[0]-i, self.position[1]-i)) == None:
                    legal_moves_list.append((self.position[0]-i, self.position[1]-i))
                elif self.chessboard.get_piece((self.position[0]-i, self.position[1]-i)) != self.color:
                    legal_moves_list.append((self.position[0]-i, self.position[1]-i))
                    break
                else:
                    break

            for i in range(1, 9): # down_right
                if self.chessboard.get_piece((self.position[0]+i, self.position[1]-i)) == None:
                    legal_moves_list.append((self.position[0]+i, self.position[1]-i))
                elif self.chessboard.get_piece((self.position[0]+i, self.position[1]-i)) != self.color:
                    legal_moves_list.append((self.position[0]+i, self.position[1]-i))
                    break
                else:
                    break

            for i in range(1, 9): # up_left
                if self.chessboard.get_piece((self.position[0]-i, self.position[1]+i)) == None:
                    legal_moves_list.append((self.position[0]-i, self.position[1]+i))
                elif self.chessboard.get_piece((self.position[0]-i, self.position[1]+i)) != self.color:
                    legal_moves_list.append((self.position[0]-i, self.position[1]+i))
                    break
                else:
                    break

            for i in range(1, 9): # up_right
                if self.chessboard.get_piece((self.position[0]+i, self.position[1]+i)) == None:
                    legal_moves_list.append((self.position[0]+i, self.position[1]+i))
                elif self.chessboard.get_piece((self.position[0]+i, self.position[1]+i)) != self.color:
                    legal_moves_list.append((self.position[0]+i, self.position[1]+i))
                    break
                else:
                    break


        return legal_moves_list