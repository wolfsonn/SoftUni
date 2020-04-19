flowers = str(input())  # Roses, Dahlias, Tulips, Narcissus, Gladiolus
number_of_flowers = int(input())
budget = int(input())
discount = float()
price = float()
if flowers == 'Roses':
    price = 5
    if number_of_flowers > 80:
        discount = 0.10
    else:
        discount = 0.00
elif flowers == 'Dahlias':
    price = 3.80
    if number_of_flowers > 90:
        discount = 0.15
    else:
        discount = 0.00
elif flowers == 'Tulips':
    price = 2.80
    if number_of_flowers > 80:
        discount = 0.15
    else:
        discount = 0
elif flowers == 'Narcissus':
    price = 3
    if number_of_flowers < 120:
        discount = -0.15
    else:
        discount = 0
else:
    price = 2.50
    if number_of_flowers < 80:
        discount = -0.20
    else:
        discount = 0
total_flowers_price = number_of_flowers * price * (1 - discount)
price_budget_delta = abs(budget - total_flowers_price)
if budget >= total_flowers_price:
    print(f'Hey, you have a great garden with {number_of_flowers} {flowers} and {price_budget_delta:.2f} leva left.')
else:
    print(f'Not enough money, you need {price_budget_delta:.2f} leva more.')