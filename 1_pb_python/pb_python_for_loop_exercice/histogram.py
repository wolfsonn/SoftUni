count = int(input())  # 1 <= n <= 1000
p1 = 0  # number < 200
p2 = 0  # 200 <= number <= 399
p3 = 0  # 400 <= number <= 599
p4 = 0  # 600 <= number <= 799
p5 = 0  # number >= 800
for numbers in range(count):
    number = int(input())
    if number < 200:
        p1 += 1 * (100 / count)
    elif 200 <= number <= 399:
        p2 += 1 * (100 / count)
    elif 400 <= number <= 599:
        p3 += 1 * (100 / count)
    elif 600 <= number <= 799:
        p4 += 1 * (100 / count)
    else:
        p5 += 1 * (100 / count)
print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
