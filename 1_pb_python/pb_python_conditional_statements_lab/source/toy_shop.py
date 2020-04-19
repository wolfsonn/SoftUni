vacation_price = float(input())
puzzles_number = int(input())
talking_dolls_number = int(input())
teddy_bears_number = int(input())
minions_number = int(input())
trucks_number = int(input())
ordered_toys_number = int(puzzles_number + talking_dolls_number + teddy_bears_number + minions_number + trucks_number)
puzzles_price = 2.60
talking_dolls_price = 3.00
teddy_bears_price = 4.10
minions_price = 8.20
trucks_price = 2.00
ordered_toys_price = float(puzzles_number * puzzles_price + talking_dolls_number * talking_dolls_price + teddy_bears_number * teddy_bears_price + minions_number * minions_price + trucks_number * trucks_price)
if ordered_toys_number >= 50:
    gains = float(ordered_toys_price * 0.75)
else:
    gains = ordered_toys_price
rent = float(gains * 0.10)
vacation_money = float(gains - rent)
leftover_money = float(vacation_money - vacation_price)
if leftover_money >= 0:
    print(f'Yes! {leftover_money:.2f} lv left.')
else:
    leftover_money = abs(leftover_money)
    print(f'Not enough money! {leftover_money:.2f} lv needed.')