def translate(move_str): # translate "b3, b4", "b3b4" or "b3 should go to b4" into position and new_position
    if type(move_str) is str:
        if move_str[0] in "ABCDEFGHabcdefgh" and move_str[len(move_str) - 2] in "ABCDEFGHabcdefgh" and move_str[1] in "12345678" and move_str[len(move_str) - 1] in "12345678":
            move_str = move_str.lower()
            position = (ord(move_str[0]) - ord("a"), int(move_str[1]) - 1)
            new_position = (ord(move_str[len(move_str) - 2]) - ord("a"), int(move_str[len(move_str) - 1]) - 1)
            return position, new_position
    return None
    # ich hab ehrlich gesagt keine Ahnung mehr was ich hier gemacht hab aber es funktioniert!