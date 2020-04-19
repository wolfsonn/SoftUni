import sys

numbers_count = int(input())
old_sum = 0
sum = 0
max_delta = -sys.maxsize
for numbers in range(numbers_count):
    number_1 = float(input())
    number_2 = float(input())
    sum = number_1 + number_2
    max_delta = -sys.maxsize
    if sum != old_sum and old_sum != 0:
        delta = abs(old_sum - sum)
        if delta > max_delta:
            max_delta = delta
    sum = old_sum
if max_delta != -sys.maxsize:
    print(f'No, maxdiff={max_delta:.0f}')
else:
    print(f'Yes, value={sum:.0f}')
