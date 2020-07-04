from collections import deque

starting_water = int(input())
names = deque()
while True:
    command = input()
    if command == 'Start':
        while True:
            index = 0
            command = input()
            if command == 'End':
                print(f'{starting_water} liters left')
                break
            elif len(command.split(' ')) < 2:
                if starting_water - int(command) >= 0:
                    print(f'{names.popleft()} got water')
                    starting_water -= int(command)
                else:
                    print(f'{names.popleft()} must wait')
            else:
                starting_water += int(command.split(' ')[1])
        break
    else:
        names.append(command)