numbers_count = int(input())
sum_left = 0
sum_right = 0
number = 0
for numbers in range(numbers_count):
    number = int(input())
    sum_left += int(number)
for numbers in range(numbers_count + 1, numbers_count * 2 + 1):
    number = int(input())
    sum_right += int(number)
diff = abs(sum_left - sum_right)
if sum_left == sum_right:
    print(f'Yes, sum = {sum_left}')
else:
    print(f'No, diff = {diff}')
