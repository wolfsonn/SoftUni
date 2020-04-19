budget = int(input())
season = str(input())
fishermen = int(input())
if season == 'Spring':
    season_price = 3000
    if fishermen <= 6:
        discount = 0.10
    elif fishermen <= 11:
        discount = 0.15
    else:
        discount = 0.25
elif season == 'Summer' or season == 'Autumn':
    season_price = 4200
    if fishermen <= 6:
        discount = 0.10
    elif fishermen <= 11:
        discount = 0.15
    else:
        discount = 0.25
else:
    season_price = 2600
    if fishermen <= 6:
        discount = 0.10
    elif fishermen <= 11:
        discount = 0.15
    else:
        discount = 0.25
if fishermen % 2 == 0 and season != 'Autumn':
    extra_discount = 0.05
else:
    extra_discount = 0
total_price = season_price * (1 - discount) * (1 - extra_discount)
delta = abs(budget - total_price)
if budget >= total_price:
    print(f'Yes! You have {delta:.2f} leva left.')
else:
    print(f'Not enough money! You need {delta:.2f} leva.')