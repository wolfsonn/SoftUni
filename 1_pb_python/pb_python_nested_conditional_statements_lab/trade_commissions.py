city = str(input())
sales = float(input())
commission_percent = float()
valid_city = city == 'Sofia' or city == 'Varna' or city == 'Plovdiv'
valid_sales = sales >= 0
if not valid_city:
    print('error')
elif not valid_sales:
    print('error')
else:
    if city == 'Sofia':
        if 0 <= sales <= 500:
            commission_percent = 5
        elif sales <= 1000:
            commission_percent = 7
        elif sales <= 10000:
            commission_percent = 8
        else:
            commission_percent = 12
    elif city == 'Varna':
        if 0 <= sales <= 500:
            commission_percent = 4.5
        elif sales <= 1000:
            commission_percent = 7.5
        elif sales <= 10000:
            commission_percent = 10
        else:
            commission_percent = 13
    else:
        if 0 <= sales <= 500:
            commission_percent = 5.5
        elif sales <= 1000:
            commission_percent = 8
        elif sales <= 10000:
            commission_percent = 12
        else:
            commission_percent = 14.5
    commission = float(commission_percent * sales / 100)
    print(f'{commission:.2f}')