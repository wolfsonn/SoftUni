raw_stock = (input()).split(" ")
stock = {}
for i in range(0, len(raw_stock), 2):
    key = raw_stock[i]
    value = raw_stock[i + 1]
    stock[key] = int(value)
search_items = (input()).split(" ")
for item in search_items:
    if item in stock:
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
