width = int(input())
length = int(input())
number_of_pieces = int(width * length)
pieces_eaten = ()
pieces_left = int(number_of_pieces)
while pieces_left > 0 and pieces_eaten != 'STOP':
    pieces_eaten = input()
    if pieces_eaten == 'STOP':
        print(f'{pieces_left} pieces are left.')
        break
    pieces_left -= int(pieces_eaten)
    if pieces_left <= 0:
        delta = abs(pieces_left)
        print(f'No more cake left! You need {delta} pieces more.')
        break
