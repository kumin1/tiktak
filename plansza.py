def draw_board(miejsca):
    board = (f"|{miejsca[1]}|{miejsca[2]}|{miejsca[3]}|\n"
             f"|{miejsca[4]}|{miejsca[5]}|{miejsca[6]}|\n"
             f"|{miejsca[7]}|{miejsca[8]}|{miejsca[9]}|")
    print(board)

def check_turn(turn):
    if turn % 2 == 0: return '0'
    else: return 'X'
def check_for_win(miejsca):
    if (miejsca[1] == miejsca[2] == miejsca[3]) \
       or (miejsca[4] == miejsca[5] == miejsca[6]) \
       or (miejsca[7] == miejsca[8] == miejsca[9]):
        return True
    elif (miejsca[1] == miejsca[4] == miejsca[7]) \
       or (miejsca[2] == miejsca[5] == miejsca[8]) \
       or (miejsca[3] == miejsca[6] == miejsca[9]):
        return True
    elif (miejsca[1] == miejsca[5] == miejsca[9]) \
       or (miejsca[3] == miejsca[5] == miejsca[7]):
        return True
    else: return False