emails = {}
send = True
while send:
    command = input()
    if command == "Statistics":
        send = False
        break
    tokens = command.split("->")
    if tokens[0] == "Add":
        username = tokens[1]
        if username not in emails:
            emails[username] = []
        else:
            print(f"{username} is already registered")
    elif tokens[0] == "Send":
        username = tokens[1]
        email = tokens[2]
        emails[username].append(email)
    elif tokens[0] == "Delete":
        username = tokens[1]
        if username not in emails.keys():
            print(f"{username} not found!")
        else:
            emails.pop(username)
print(f"Users count: {len(emails.keys())}")
emails_sorted = sorted(emails.items(), key=lambda x: (-len(x[1]), x[0]))
for (user, email) in emails_sorted:
    print(f"{user}")
    for user in emails_sorted:
        print("")

