age = int(input())
price = float(input())
toy_price = int(input())
money_count = 1
savings = 0
for birthday in range(1, age + 1, 2):  # odd
    savings += toy_price
for birthday in range(2, age + 1, 2):  # even
    savings += ((money_count * 10) - 1)
    money_count += 1
delta = abs(price - savings)
if savings >= price:
    print(f'Yes! {delta:.2f}')
else:
    print(f'No! {delta:.2f}')
