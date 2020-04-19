import re
barcode_count = int(input())
regex = r"@#+[A-Z][A-Za-z0-9]{4}[A-Za-z0-9]*[A-Z]@#+"
for _ in range(barcode_count):
    barcode = input()
    match = re.findall(regex, barcode)
    if not match:
        print("Invalid barcode")
    else:
        product_group = "".join([ch for ch in barcode if ch.isnumeric()])
        if product_group == "":
            product_group = "00"
        print(f"Product group: {product_group}")