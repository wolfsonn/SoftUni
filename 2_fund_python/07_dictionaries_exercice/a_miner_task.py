resources = {}

while True:
    command = input()
    if command == "stop":
        break
    else:
        resource = command
        quantity = int(input())
        if resource not in resources:
            resources[resource] = 0
        resources[resource] += quantity
for (resource, quantity) in resources.items():
    print(f"{resource} -> {resources[resource]}")