screening_type = str(input())
rows = int(input())
columns = int(input())
ticket_price = float()
if screening_type == 'Premiere':
    ticket_price = 12.00
elif screening_type == 'Normal':
    ticket_price = 7.50
else:
    ticket_price = 5.00
full_house_price = ticket_price * rows * columns
print(f'{full_house_price:.2f} leva')