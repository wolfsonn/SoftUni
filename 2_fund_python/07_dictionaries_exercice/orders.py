product_prices = {}
product_quantities = {}

while True:
    command = input()
    if command == "buy":
        break
    product_info = command.split(" ")
    product_name = product_info[0]
    product_price = float(product_info[1])
    product_quantity = float(product_info[2])
    if product_name not in product_prices:
        product_quantities[product_name] = product_quantity
    else:
        product_quantities[product_name] += product_quantity
    product_prices[product_name] = product_price
for (product, price) in product_prices.items():
    print(f"{product} -> {product_prices[product] * product_quantities[product]:.2f}")
