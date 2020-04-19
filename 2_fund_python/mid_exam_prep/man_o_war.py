pirate_status = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))
max_health = int(input())
game_on = True
while game_on:
    command = input()
    command_list = command.split()
    if command == 'Retire':
        print(f'Pirate ship status: {sum(pirate_status)}')
        print(f'Warship status: {sum(warship_status)}')
        game_on = False
        break
    elif command_list[0] == 'Fire':
        if 0 <= int(command_list[1]) < len(warship_status):
            warship_status[int(command_list[1])] -= int(command_list[2])
            if warship_status[int(command_list[1])] <= 0:
                print('You won! The enemy ship has sunken.')
                game_on = False
                break
    elif command_list[0] == 'Defend':
        if 0 <= int(command_list[1]) < len(pirate_status) and 0 <= int(command_list[2]) < len(pirate_status):
            pirate_status[int(command_list[1]):(int(command_list[2]) + 1)] = [i - int(command_list[3]) for i in pirate_status[int(command_list[1]):(int(command_list[2]) + 1)]]
            for i in pirate_status:
                if i <= 0:
                    print('You lost! The pirate ship has sunken.')
                    game_on = False
                    break
    elif command_list[0] == 'Repair':
        if 0 <= int(command_list[1]) < len(pirate_status):
            pirate_status[int(command_list[1])] += int(command_list[2])
            if pirate_status[int(command_list[1])] > max_health:
                pirate_status[int(command_list[1])] = max_health
    elif command == 'Status':
        print(f'{len([s for s in pirate_status if s < max_health * 0.2])} sections need repair.')
