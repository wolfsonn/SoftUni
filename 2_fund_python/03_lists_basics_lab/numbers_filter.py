n = int(input())
even = []
odd = []
negative = []
positive = []
for i in range(n):
    number = int(input())
    if number >= 0 and number % 2 == 0:
        even.append(number)
        positive.append(number)
    elif number >= 0 and number % 2 == 1:
        odd.append(number)
        positive.append(number)
    elif number < 0 and number % 2 == 0:
        even.append(number)
        negative.append(number)
    else:
        odd.append(number)
        negative.append(number)
command = str(input())
if command == 'even':
    print(even)
elif command == 'odd':
    print(odd)
elif command == 'negative':
    print(negative)
else:
    print(positive)