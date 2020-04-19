fruit = str(input())
valid_fruit = fruit == 'banana' or fruit == 'apple' or fruit == 'orange' or fruit == 'grapefruit' or fruit == 'kiwi' or fruit == 'pineapple' or fruit == 'grapes'
day_of_the_week = str(input())
valid_day_of_the_week = day_of_the_week == 'Monday' or day_of_the_week == 'Tuesday' or day_of_the_week == 'Wednesday' or day_of_the_week == 'Thursday' or day_of_the_week == 'Friday' or day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday'
quantity = float(input())
price = float()
weekend = day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday'
if not valid_fruit:
    print('error')
elif not valid_day_of_the_week:
    print('error')
else:
    if not weekend:
        if fruit == 'banana':
            price = 2.50
        elif fruit == 'apple':
            price = 1.20
        elif fruit == 'orange':
            price = 0.85
        elif fruit == 'grapefruit':
            price = 1.45
        elif fruit == 'kiwi':
            price = 2.70
        elif fruit == 'pineapple':
            price = 5.50
        else:
            price = 3.85
    else:
        if fruit == 'banana':
            price = 2.70
        elif fruit == 'apple':
            price = 1.25
        elif fruit == 'orange':
            price = 0.90
        elif fruit == 'grapefruit':
            price = 1.60
        elif fruit == 'kiwi':
            price = 3.00
        elif fruit == 'pineapple':
            price = 5.60
        else:
            price = 4.20
    total = price * quantity
    print(f'{total:.2f}')