size = int(input())

territory = []
food = 0
over = False

for _ in range(size):
    territory.append([x for x in input()])
sl = []  # row, column
found_s = False
for row in range(size):
    if found_s:
        break
    for column in range(size):
        if territory[row][column] == "S":
            sl.append(row)
            sl.append(column)
            found_s = True

while not over and food < 10:

    command = input()
    if command == 'up':
        territory[sl[0]][sl[1]] = "."
        if sl[0] == 0:
            over = True
            break
        else:
            sl[0] -= 1
    elif command == 'down':
        territory[sl[0]][sl[1]] = "."
        if sl[0] == size - 1:
            over = True
            break
        else:
            sl[0] += 1
    elif command == 'left':
        territory[sl[0]][sl[1]] = "."
        if sl[1] == 0:
            over = True
            break
        else:
            sl[1] -= 1
    elif command == 'right':
        territory[sl[0]][sl[1]] = "."
        if sl[1] == size - 1:
            over = True
            break
        else:
            sl[1] += 1

    if territory[sl[0]][sl[1]] == "B":
        territory[sl[0]][sl[1]] = "."
        bl = []
        found_b = False
        for row in range(size):
            if found_b:
                break
            for column in range(size):
                if territory[row][column] == "B":
                    bl.append(row)
                    bl.append(column)
                    found_b = True
        territory[bl[0]][bl[1]] = "."
        sl[0] = bl[0]
        sl[1] = bl[1]

    if territory[sl[0]][sl[1]] == "*":
        food += 1
        if food == 10:
            territory[sl[0]][sl[1]] = "S"
if over:
    print("Game over!")
else:
    print("You won! You fed the snake.")

print(f"Food eaten: {food}")

for i in range(size):
    for j in range(size):
        print(territory[i][j], end="")
    print()