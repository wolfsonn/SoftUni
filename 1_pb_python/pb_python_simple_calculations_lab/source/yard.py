area = float(input())
regular_price = float(7.61)
discount_percentage = float(0.18)
final_price = float(area * regular_price * (1 - discount_percentage))
discount = float(area * regular_price * discount_percentage)
print(f'The final price is: {final_price:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')