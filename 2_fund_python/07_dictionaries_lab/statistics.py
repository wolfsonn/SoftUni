stock = {}

while True:
    command = input()
    if command == 'statistics':
        break
    else:
        product_in = command.split(": ")
        product = product_in[0]
        quantity = int(product_in[1])
        if product not in stock:
            stock[product] = 0
        stock[product] += quantity
print("Products in stock:")
for (product, quantity) in stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(stock.keys())}")
print(f"Total Quantity: {sum(stock.values())}")