age = float(input())
if 0 < age <= 14:
    person_type = 'kid'
elif age <= 18:
    person_type = 'teen'
elif age <= 21:
    person_type = 'young adult'
else:
    person_type = 'adult'

if person_type == 'kid':
    drink_type = 'toddy'
elif person_type == 'teen':
    drink_type = 'coke'
elif person_type == 'young adult':
    drink_type = 'beer'
else:
    drink_type = 'whisky'

print(f'drink {drink_type}')
