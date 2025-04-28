import os
import time


def print_possible_moves (list_of_moves):
    for item in list_of_moves:
        print(item)

turn = True

white_pieces = ['♖','♖','♘','♘','♗','♗','♔','♕','♙','♙','♙','♙','♙','♙','♙','♙']
white_captured_pieces = []
white_pieces_position = ['A1','H1','B1','G1','C1','F1','E1','D1','A2','B2','C2','D2','E2','F2','G2','H2']

black_pieces = ['♜','♜','♞','♞','♝','♝','♚','♛','♟','♟','♟','♟','♟','♟','♟','♟']
black_captured_pieces = []
black_pieces_position = ['A8','H8','B8','G8','C8','F8','D8','E8','A7','B7','C7','D7','E7','F7','G7','H7']

while True:
    os.system('cls')

    for i in range(0,8):
        for letter in 'ABCDEFGH':
            if f'{letter}{i+1}' in white_pieces_position:
                print(white_pieces[white_pieces_position.index(f'{letter}{i+1}')], end=' ')
            elif f'{letter}{i+1}' in black_pieces_position:
                print(black_pieces[black_pieces_position.index(f'{letter}{i+1}')], end=' ')
            else:
                print (f'{letter}{i+1} ',end=' ')
        print ('\n')
    time.sleep(3)
    
    if turn:
        print('It is white player\'s turn, Chose a piece to move')
        choice = input('')

        if choice in white_pieces_position :
            if white_pieces[white_pieces_position.index(choice)] == '♙':
                if choice[1] == '2':
                    possible_moves = []
                    for i in range(0,2):
                        if f'{choice[0]}{int(choice[1])+1+i}' not in black_pieces_position:
                            possible_moves.append(f'{choice[0]}{int(choice[1])+1+i}')

                    attacks = [f'{'ABCDEFGH'['ABCDEFGH'.index(choice[0])+1]}{int(choice[1])+1}', 
                               f'{'ABCDEFGH'['ABCDEFGH'.index(choice[0])-1]}{int(choice[1])+1}']
                    for attack in attacks:
                        if attack in black_pieces_position:
                            possible_moves.append(attack)

                    print('Possible Moves:')
                    print_possible_moves(possible_moves)
                    destination = input('Chose your destination: ')
                    if destination in possible_moves:
                        white_pieces_position[white_pieces_position.index(choice)] = destination
                        turn = False
                    else:
                        print('You can not do this')
                        time.sleep(3)
                else:
                    possible_moves = []
                    for i in range(0,2):
                        if f'{choice[0]}{int(choice[1])+1+i}' not in black_pieces_position:
                            possible_moves.append(f'{choice[0]}{int(choice[1])+1+i}')
                    attacks = [f'{'ABCDEFGH'['ABCDEFGH'.index(choice[0])+1]}{int(choice[1])+1}', 
                               f'{'ABCDEFGH'['ABCDEFGH'.index(choice[0])-1]}{int(choice[1])+1}']
                    for attack in attacks:
                        if attack in black_pieces_position:
                            possible_moves.append(attack)
                    
                    print('Possible Moves:')
                    print_possible_moves(possible_moves)
                    destination = input('Chose your destination')
                    if destination in possible_moves:
                        white_pieces_position[white_pieces_position.index(choice)] = destination
                        turn = False
                    else:
                        print('You can not do this')
                        time.sleep(3)
        else:
            print('U have no piece here, chose another location')
            time.sleep(3)