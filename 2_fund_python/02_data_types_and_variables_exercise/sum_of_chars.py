lines = int(input())
sum = 0
for i in range(lines):
    char = input()
    sum += ord(char)
print(f'The sum equals: {sum}')