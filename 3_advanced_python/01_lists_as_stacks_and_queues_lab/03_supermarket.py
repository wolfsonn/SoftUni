def names_list():
    names = []
    while True:
        command = input()
        if command == 'End':
            print(f'{len(names)} people remaining.')
            break
        elif command == 'Paid':
            for name in names:
                print(name)
            names = []
        else:
            names.append(command)

names_list()