championship_stage = str(input())  # Quarter final, Semi final, Final
ticket_type = str(input())  # Standard, Premium, VIP
ticket_count = int(input())
picture = str(input())  # Y, N
ticket_price = ()
if championship_stage == 'Quarter final':
    if ticket_type == 'Standard':
        ticket_price = 55.50
    elif ticket_type == 'Premium':
        ticket_price = 105.20
    else:
        ticket_price = 118.90
elif championship_stage == 'Semi final':
    if ticket_type == 'Standard':
        ticket_price = 75.88
    elif ticket_type == 'Premium':
        ticket_price = 125.22
    else:
        ticket_price = 300.40
else:
    if ticket_type == 'Standard':
        ticket_price = 110.10
    elif ticket_type == 'Premium':
        ticket_price = 160.66
    else:
        ticket_price = 400.00
total_ticket_price = ticket_count * ticket_price
if total_ticket_price > 4000:
    discount_price = total_ticket_price * 0.75
    total_price = discount_price
elif total_ticket_price > 2500:
    discount_price = total_ticket_price * 0.90
    if picture == 'Y':
        total_price = discount_price + (ticket_count * 40)
    else:
        total_price = discount_price
else:
    if picture == 'Y':
        total_price = total_ticket_price + (ticket_count * 40)
    else:
        total_price = total_ticket_price
print(f'{total_price:.2f}')