num = float(input())
num_type_one = str()

if num < 0 and abs(num) < 1:
    print('small negative')
elif num < 0 and abs(num) > 1000000:
    print('large negative')
elif num < 0:
    print('negative')
elif num == 0:
    print('zero')
elif num > 0 and abs(num) < 1:
    print('small positive')
elif num > 0 and abs(num) > 1000000:
    print('large positive')
else:
    print('positive')