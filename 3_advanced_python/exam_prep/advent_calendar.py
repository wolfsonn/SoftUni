def fix_calendar(num):
    i = -1
    swap = 0
    for _ in range(len(num) - 1):
        i += 1
        if num[i] > num[i + 1]:
            num[i], num[i + 1] = num[i + 1], num[i]
            swap = 1
    if swap != 0:
        fix_calendar(num)

    return num


numbers = [6, 3, 8, 2, 9, 0, 45, 1]
print(fix_calendar(numbers))
