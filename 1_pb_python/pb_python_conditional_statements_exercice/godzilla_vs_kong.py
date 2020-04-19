budget = float(input())
trees = int(input())
price_per_clothing = float(input())
decor = budget * 0.10
if trees <= 150:
    clothing_price = trees * price_per_clothing
else:
    clothing_price = trees * price_per_clothing * 0.90
delta = abs(budget - decor - clothing_price)
if clothing_price + decor > budget:
    print('Not enough money!')
    print(f'Wingard needs {delta:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {delta:.2f} leva left.')