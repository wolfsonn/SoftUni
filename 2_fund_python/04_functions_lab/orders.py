product_input = input()
quantity_input = input()


def price_calc(product, quantity):
    price = None
    if product == 'coffee':
        price = 1.50
    elif product == 'water':
        price = 1.00
    elif product == 'coke':
        price = 1.40
    elif product == 'snacks':
        price = 2.00
    return float(price) * float(quantity)


print(f'{price_calc(product_input, quantity_input):.2f}')

