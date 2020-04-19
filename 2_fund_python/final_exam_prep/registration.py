import re
number_of_lines = int(input())
registrations = 0
for _ in range(number_of_lines):
    user_in = input()
    regex = r"(U\$[A-Z][a-z]{2}[a-z]*U\$)(P@\$\w{5}\w*\dP@\$)"
    matches = re.findall(regex, user_in)
    if not matches:
        print("Invalid username or password")
    else:
        print("Registration was successful")
        registrations += 1
        user, password = matches[0]
        print(f"Username: {user[2:-2]}, Password: {password[3:-3]}")
print(f"Successful registrations: {registrations}")
