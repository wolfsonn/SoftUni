loot = input().split('|')

while True:
    command = input()
    command_list = command.split()
    if command == 'Yohoho!':
        break
    elif command_list[0] == 'Loot':
        for l in command_list[1::]:
            if l not in loot:
                loot.insert(0, l)
    elif command_list[0] == 'Drop' and 0 <= int(command_list[1]) <= len(loot):
        loot.append(loot.pop(int(command_list[1])))
    elif command_list[0] == 'Steal':
        if int(command_list[1]) > len(loot):
            command_list[1] = str(len(loot))
        print(', '.join(loot[len(loot) - int(command_list[1]):len(loot)]))
        loot = loot[0:(len(loot) - int(command_list[1]))]
if len(loot) == 0:
    print('Failed treasure hunt.')
else:
    treasure_gain = 0
    for i in loot:
        treasure_gain += len(i)
    print(f'Average treasure gain: {treasure_gain / len(loot):.2f} pirate credits.')
