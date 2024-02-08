from plansza import draw_board, check_turn, check_for_win
import os

miejsca = {1 : '1',2 : '2',3 : '3',4 : '4',5 : '5',6 : '6',7 : '7',8 : '8',9 : '9',}

active = True
complete = False
turn = 0
prev_turn = -1

while active:
    os.system('cls' if os.name == 'nt' else clear)
    draw_board(miejsca)
    if prev_turn == turn:
        print('nieprawidlowe miejsce, wybierz inne')
    prev_turn = turn
    print("tura gracza ", str((turn % 2) +1)), "wybierz miejsce albo napisz q aby wyjsc"
    choice = input()
    if choice == 'q':
        active = False
    elif str.isdigit(choice) and int(choice) in miejsca:
        if not miejsca[int(choice)] in {"X","O"}:
            turn += 1
            miejsca[int(choice)] = check_turn(turn)
    if check_for_win(miejsca): playing, complete = False,True
    if turn>8: playing = False
if complete:
    if check_turn(turn) == 'X': print('gracz 1 wygrywa')
    else: print('gracz 2 wygrywa')
else:
    print('niema wygranego')

    