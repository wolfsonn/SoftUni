numbers_count = int(input())
counter = 0
max_number = ()
while counter < numbers_count:
    number = int(input())
    if counter == 0:
        max_number = number
    else:
        if number > max_number:
            max_number = number
    counter += 1
print(max_number)