

def list_to_string(list):
    liststring = ""
    for item in list:
        liststring += item
        liststring += "  "
    return liststring

def get_piece_type(piece):
    complete_type = str(type(piece))
    i = len(complete_type) - 3
    complete = False
    basic_type = ""
    while not complete:
        if complete_type[i] == ".":
            complete = True
            return basic_type
        basic_type = complete_type[i] + basic_type
        i -= 1

