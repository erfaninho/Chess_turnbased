
white_pieces = ['♖1','♖2','♘1','♘2','♗1','♗2','♔','♕','♙1','♙2','♙3','♙4','♙5','♙6','♙7','♙8']
white_captured_pieces = []
white_pieces_position = ['A1','H1','B1','G1','C1','F1','E1','D1','A2','B2','C2','D2','E2','F2','G2','H2']

black_pieces = ['♜1','♜2','♞1','♞2','♝1','♝2','♚','♛','♟1','♟2','♟3','♟4','♟5','♟6','♟7','♟8']
black_captured_pieces = []
black_pieces_position = ['A8','H8','B8','G8','C8','F8','D8','E8','A7','B7','C7','D7','E7','F7','G7','H7']

for i in range(0,8):
    for letter in 'ABCDEFGH':
        if f'{letter}{i+1}' in white_pieces_position:
            print(white_pieces[white_pieces_position.index(f'{letter}{i+1}')], end=' ')
        elif f'{letter}{i+1}' in black_pieces_position:
            print(black_pieces[black_pieces_position.index(f'{letter}{i+1}')], end=' ')
        else:
            print (f'{letter}{i+1} ',end=' ')
    print ('\n')

input('press Enter key to end')