number_of_tables = int(input())
table_length = float(input())
table_width = float(input())
cloth_length = float(table_length + 0.6)
cloth_width = float(table_width + 0.6)
square_side = float(table_length / 2)
cloth_price = float(cloth_length * cloth_width * 7)
square_price = float(square_side * square_side * 9)
usd = float (1.85)
total_usd = float(number_of_tables * (cloth_price + square_price))
total_bgn = float(total_usd * usd)
print(f'{total_usd:.2f} USD')
print(f'{total_bgn:.2f} BGN')