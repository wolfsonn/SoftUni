numbers_count = int(input())
counter = 0
min_number = ()
while counter < numbers_count:
    number = int(input())
    if counter == 0:
        min_number = number
    else:
        if number < min_number:
            min_number = number
    counter += 1
print(min_number)