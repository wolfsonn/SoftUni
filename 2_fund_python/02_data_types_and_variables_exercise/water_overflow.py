lines = int(input())
capacity = 255
total = 0
for i in range(0, lines):
    quantity = input()
    total += int(quantity)
    if total > capacity:
        print("Insufficient capacity!")
        total -= int(quantity)
if total < 255:
    print(total)
else:
    print(255)