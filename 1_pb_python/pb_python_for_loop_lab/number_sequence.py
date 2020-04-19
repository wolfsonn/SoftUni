numbers_count = int(input())
smallest_number = 999999999
biggest_number = -999999999
number = ()
for numbers in range(numbers_count):
    number = int(input())
    if number < int(smallest_number):
        smallest_number = number
    if number > int(biggest_number):
        biggest_number = number
print(f'Max number: {biggest_number}')
print(f'Min number: {smallest_number}')
