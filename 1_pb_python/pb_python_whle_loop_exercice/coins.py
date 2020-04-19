import math
change = float(input())
coin_pieces = 0
while change >= 2:
    coin_pieces += 1
    change = round(change - 2, 2)
while change >= 1:
    coin_pieces += 1
    change = round(change - 1, 2)
while change >= 0.50:
    coin_pieces += 1
    change = round(change - 0.50, 2)
while change >= 0.20:
    coin_pieces += 1
    change = round(change - 0.20, 2)
while change >= 0.10:
    coin_pieces += 1
    change = round(change - 0.10, 2)
while change >= 0.05:
    coin_pieces += 1
    change = round(change - 0.05, 2)
while change >= 0.02:
    coin_pieces += 1
    change = round(change - 0.02, 2)
while change >= 0.01:
    coin_pieces += 1
    change = round(change - 0.01, 2)
print(coin_pieces)
