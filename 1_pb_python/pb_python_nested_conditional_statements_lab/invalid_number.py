number = float(input())
valid = 200 >= number >= 100 or number == 0
if not valid:
    print('invalid')