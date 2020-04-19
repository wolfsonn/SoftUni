password = input()
change = True
while change:
    command = input()
    if command == "Done":
        change = False
        break
    if command == "TakeOdd":
        password = password[1::2]
        print(password)
    else:
        tokens = command.split(" ")
        if tokens[0] == "Cut":
            index = int(tokens[1])
            length = int(tokens[2])
            password = password[:index] + password[index + length:]
            print(password)
        elif tokens[0] == "Substitute":
            substring = tokens[1]
            substitute = tokens[2]
            if substring not in password:
                print("Nothing to replace!")
            else:
                password = password.replace(substring, substitute)
                print(password)
print(f"Your password is: {password}")
