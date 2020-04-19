gifts_list = input().split()
while True:
    command = input()
    if command == 'No Money':
        break
    else:
        command_list = command.split()
        if command_list[0] == 'OutOfStock':
            for gift in range(len(gifts_list)):
                if gifts_list[gift] == command_list[1]:
                    gifts_list[gift] = 'None'
        elif command_list[0] == 'Required' and 0 <= int(command_list[2]) <= len(gifts_list) - 1:
            gifts_list[int(command_list[2])] = command_list[1]
        elif command_list[0] == 'JustInCase':
            gifts_list[len(gifts_list) - 1] = command_list[1]
print(' '.join(gift for gift in gifts_list if gift != 'None'))
