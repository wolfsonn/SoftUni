email = input()

while True:
    command = input()
    if command == "Complete":
        break
    elif command == "Make Upper":
        email = email.upper()
        print(email)
    elif command == "Make Lower":
        email = email.lower()
        print(email)
    elif command == "GetUsername":
        if "@" not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            print(email[:(email.find("@"))])
    elif command == "Encrypt":
        for char in email:
            print(ord(char), end=" ")
    else:
        tokens = command.split()
        if tokens[0] == "GetDomain":
            print(email[-int(tokens[1]):])
        elif tokens[0] == "Replace":
            print(email.replace(tokens[1], "-"))
