hearts = list(map(int, input().split('@')))
jumping = True
index = 0
houses = len(hearts)
while jumping:
    command = input()
    if command == 'Love!':
        jumping = False
        break
    else:
        command_list = command.split()
        index = int(index + int(command_list[1]))
        if index > len(hearts) - 1:
            index = 0
        if hearts[index] == 0:
            print(f'Place {index} already had Valentine\'s day.')
        else:
            hearts[index] -= 2
            if hearts[index] < 0:
                hearts[index] = 0
            if hearts[index] == 0:
                print(f'Place {index} has Valentine\'s day.')
print(f'Cupid\'s last position was {index}.')
if sum(hearts) == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {len([i for i in hearts if i != 0])} places.')
