budget = float(input())
season = str(input())
destination = str()
accommodation = str()
money_spent = float()
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        accommodation = 'Camp'
        money_spent = budget * 0.30
    else:
        accommodation = 'Hotel'
        money_spent = budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        accommodation = 'Camp'
        money_spent = budget * 0.40
    else:
        accommodation = 'Hotel'
        money_spent = budget * 0.80
else:
    destination = 'Europe'
    accommodation = 'Hotel'
    money_spent = budget * 0.90
print(f'Somewhere in {destination}')
print(f'{accommodation} - {money_spent:.2f}')