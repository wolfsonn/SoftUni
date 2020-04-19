guest_performer_price = int(input())
people_in_group = ()
total_people = 0
price_per_person = ()
total_price = 0
while people_in_group != 'The restaurant is full':
    people_in_group = input()
    delta = abs(total_price - guest_performer_price)
    if people_in_group == 'The restaurant is full':
        if total_price >= guest_performer_price:
            print(f'You have {total_people} guests and {delta} leva left.')
        else:
            print(f'You have {total_people} guests and {total_price} leva income, but no singer.')
            break
    elif int(people_in_group) < 5:
        price_per_person = 100
        total_price += int(people_in_group) * int(price_per_person)
        total_people += int(people_in_group)
    else:
        price_per_person = 70
        total_price += int(people_in_group) * int(price_per_person)
        total_people += int(people_in_group)
