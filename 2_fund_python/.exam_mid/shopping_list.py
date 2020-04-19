shopping_list = input().split('!')
shopping = False
while not shopping:
    command = input()
    command_list = command.split()
    if command == 'Go Shopping!':
        shopping = True
    elif command_list[0] == 'Urgent' and command_list[1] not in shopping_list:
        shopping_list.insert(0, command_list[1])
    elif command_list[0] == 'Unnecessary' and command_list[1] in shopping_list:
        shopping_list.remove(command_list[1])
    elif command_list[0] == 'Correct' and command_list[1] in shopping_list:
        shopping_list[shopping_list.index(command_list[1])] = command_list[2]
    elif command_list[0] == 'Rearrange' and command_list[1] in shopping_list:
        shopping_list.append(shopping_list.pop(shopping_list.index(command_list[1])))
print(', '.join(shopping_list))
