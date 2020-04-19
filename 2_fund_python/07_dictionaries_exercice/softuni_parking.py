parking_register = {}
commands_number = int(input())
for _ in range(commands_number):
    command = input().split(" ")
    if command[0] == "register":
        username = command[1]
        plate = command[2]
        if username in parking_register:
            print(f"ERROR: already registered with plate number {plate}")
        else:
            parking_register[username] = plate
            print(f"{username} registered {parking_register[username]} successfully")
    elif command[0] == "unregister":
        username = command[1]
        if username not in parking_register:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            parking_register.pop(username)
for (user, plate) in parking_register.items():
    print(f"{user} => {parking_register[user]}")
