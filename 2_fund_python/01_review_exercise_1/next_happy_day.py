number = int(input())
while True:
    number += 1
    number_len = len(str(number))
    unique_len = len(set(str(number)))
    if number_len == unique_len:
        print(number)
        break