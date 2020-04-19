days = int(input())
nights = days - 1
nights_discount = float()
room_type = str(input())
eval = str(input())
positive_eval = eval == 'positive'
if positive_eval:
    eval_discount = -0.25
else:
    eval_discount = 0.10
if room_type == 'room for one person':
    price_per_night = 18
    nights_discount = 0
elif room_type == 'apartment':
    price_per_night = 25
    if 0 < nights < 10:
        nights_discount = 0.30
    elif nights <= 15:
        nights_discount = 0.35
    else:
        nights_discount = 0.50
else:
    price_per_night = 35
    if 0 < nights < 10:
        nights_discount = 0.10
    elif nights <= 15:
        nights_discount = 0.15
    else:
        nights_discount = 0.20
final_price = (nights * price_per_night * (1 - nights_discount)) * (1 - eval_discount)
print(f'{final_price:.2f}')