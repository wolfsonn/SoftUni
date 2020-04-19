raw_stock = (input()).split(" ")
stock = {}
for i in range(0, len(raw_stock), 2):
    key = raw_stock[i]
    value = raw_stock[i + 1]
    stock[key] = int(value)
print(stock)