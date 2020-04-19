import sys

numbers_count = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
number = float()
for numbers in range(1, numbers_count + 1):
    number = float(input())
    if numbers % 2 == 1:  # odd
        odd_sum += float(number)
        if number < odd_min:
            odd_min = float(number)
        if number > odd_max:
            odd_max = float(number)
    else:
        even_sum += float(number)
        if number < even_min:
            even_min = float(number)
        if number > even_max:
            even_max = float(number)
print(f'OddSum={odd_sum:.2f},')
if odd_min == sys.maxsize:
    print(f'OddMin=No,')
else:
    print(f'OddMin={odd_min:.2f},')
if odd_max == -sys.maxsize:
    print(f'OddMax=No,')
else:
    print(f'OddMax={odd_max:.2f},')
print(f'EvenSum={even_sum:.2f},')
if even_min == sys.maxsize:
    print(f'EvenMin=No,')
else:
    print(f'EvenMin={even_min:.2f},')
if even_max == -sys.maxsize:
    print(f'EvenMax=No')
else:
    print(f'EvenMax={even_max:.2f}')
