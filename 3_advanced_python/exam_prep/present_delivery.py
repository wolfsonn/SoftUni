size = int(input())
neighborhood = []

for _ in range(size):
    neighborhood.append([x for x in input().split(' ')])
sl = []  # row, column
found = False
for row in range(size):
    if found:
        break
    for column in range(size):
        if neighborhood[row][column] == "S":
            sl[0] = row
            sl[1] = column
            found = True

nice_kids = []
for i in range(size):
    for j in range(size):
        if neighborhood[i][j] == "V":
            nice_kids.append(neighborhood[i][j])
nice_kids_count = len(nice_kids)

while True and found:
    command = input()

    if command == "Christmas morning" or presents <= 0:
        neighborhood[sl[0]][sl[1]] = "S"
        break
    elif command == 'up' and sl[0] > 0:
        neighborhood[sl[0]][sl[1]] = "-"
        sl[0] -= 1
    elif command == 'down' and sl[0] < size:
        neighborhood[sl[0]][sl[1]] = "-"
        sl[0] += 1
    elif command == 'left' and sl[1] > 0:
        neighborhood[sl[0]][sl[1]] = "-"
        sl[1] -= 1
    elif command == 'right' and sl[1] < size:
        neighborhood[sl[0]][sl[1]] = "-"
        sl[1] += 1

    if neighborhood[sl[0]][sl[1]] == "V":
        presents -= 1
    elif neighborhood[sl[0]][sl[1]] == "X":
        continue
    elif neighborhood[sl[0]][sl[1]] == "C":
        if neighborhood[sl[0] - 1][sl[1]] == "V" or neighborhood[sl[0] - 1][sl[1]] == "X":
            presents -= 1
            neighborhood[sl[0] - 1][sl[1]] = "-"
            if presents <= 0:
                neighborhood[sl[0]][sl[1]] = "S"
                break
        if neighborhood[sl[0] + 1][sl[1]] == "V" or neighborhood[sl[0] + 1][sl[1]] == "X":
            presents -= 1
            neighborhood[sl[0] + 1][sl[1]] = "-"
            if presents <= 0:
                neighborhood[sl[0]][sl[1]] = "S"
                break
        if neighborhood[sl[0]][sl[1] - 1] == "V" or neighborhood[sl[0]][sl[1] - 1] == "X":
            presents -= 1
            neighborhood[sl[0]][sl[1] - 1] = "-"
            if presents <= 0:
                neighborhood[sl[0]][sl[1]] = "S"
                break
        if neighborhood[sl[0]][sl[1] + 1] == "V" or neighborhood[sl[0]][sl[1] + 1] == "X":
            presents -= 1
            neighborhood[sl[0]][sl[1] + 1] = "-"
            if presents <= 0:
                neighborhood[sl[0]][sl[1]] = "S"
                break
nice_kids_left = []
for i in range(size):
    for j in range(size):
        if neighborhood[i][j] == "V":
            nice_kids_left.append(neighborhood[i][j])
nice_kids_left_count = len(nice_kids_left)
if nice_kids_left_count > 0:
    print('Santa ran out of presents!')
for i in range(size):
    for j in range(size):
        print(neighborhood[i][j], end=" ")
    print()
if nice_kids_left_count == 0:
    print(f"Good job, Santa! {nice_kids_count} happy nice kid/s.")
if nice_kids_left_count > 0:
    print(f"No presents for {nice_kids_left_count} nice kid/s.")
