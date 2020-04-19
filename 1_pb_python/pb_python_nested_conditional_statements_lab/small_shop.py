product_name = str(input())
city = str(input())
quantity = float(input())
price = float()
if product_name == 'coffee':
    if city == 'Sofia':
        price = 0.50
    elif city == 'Plovdiv':
        price = 0.40
    else:
        price = 0.45
elif product_name == 'water':
    if city == 'Sofia':
        price = 0.80
    else:
        price = 0.70
elif product_name == 'beer':
    if city == 'Sofia':
        price = 1.20
    elif city == 'Plovdiv':
        price = 1.15
    else:
        price = 1.10
elif product_name == 'sweets':
    if city == 'Sofia':
        price = 1.45
    elif city == 'Plovdiv':
        price = 1.30
    else:
        price = 1.35
else:
    if city == 'Sofia':
        price = 1.60
    elif city == 'Plovdiv':
        price = 1.50
    else:
        price = 1.55
print(quantity * price)