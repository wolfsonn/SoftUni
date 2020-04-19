month = str(input())
nights = int(input())
accommodation = str()
discount = float()
price = float()
if month == 'May' or month == 'October':
    price_apartment = 65
    price_studio = 50
    if nights > 14:
        discount_apartment = 0.10
        discount_studio = 0.30
    elif nights > 7:
        discount_studio = 0.05
        discount_apartment = 0
    else:
        discount_apartment = 0
        discount_studio = 0
elif month == 'June' or month == 'September':
    price_apartment = 68.70
    price_studio = 75.20
    if nights > 14:
        discount_apartment = 0.10
        discount_studio = 0.20
    else:
        discount_apartment = 0
        discount_studio = 0
else:
    price_apartment = 77
    price_studio = 76
    if nights > 14:
        discount_apartment = 0.10
        discount_studio = 0
    else:
        discount_apartment = 0
        discount_studio = 0
total_price_apartment = (price_apartment * nights * (1 - discount_apartment))
total_price_studio = (price_studio * nights * (1 - discount_studio))
print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')