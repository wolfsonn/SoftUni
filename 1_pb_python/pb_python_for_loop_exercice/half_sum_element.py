import sys

numbers_count = int(input())
sum = 0
max_num = -sys.maxsize
for num in range(numbers_count):
    number = input()
    sum += int(number)
    if int(number) > max_num:
        max_num = int(number)
diff = abs(sum - max_num - max_num)
if max_num == sum - max_num:
    print(f'Yes')
    print(f'Sum = {max_num}')
else:
    print(f'No')
    print(f'Diff = {diff}')