numbers_count = int(input())
even_sum = 0
odd_sum = 0
for numbers in range(numbers_count):
    number = int(input())
    if numbers % 2 == 0:
        even_sum += number
    else:
        odd_sum += number
diff = abs(even_sum - odd_sum)
if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {even_sum}')
else:
    print(f'No')
    print((f'Diff = {diff}'))