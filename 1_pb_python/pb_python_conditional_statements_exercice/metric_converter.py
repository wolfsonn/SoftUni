number = float(input())
measurement_unit_1 = str(input())
measurement_unit_2 = str(input())
result = float()
if measurement_unit_1 == 'm':
    if measurement_unit_2 == 'm':
        result = number
    elif measurement_unit_2 == 'cm':
        result = number * 100
    else:
        result = number * 1000
elif measurement_unit_1 == 'cm':
    if measurement_unit_2 == 'm':
        result = number / 100
    elif measurement_unit_2 == 'cm':
        result = number
    else:
        result = number * 10
else:
    if measurement_unit_2 == 'm':
        result = number / 1000
    elif measurement_unit_2 == 'cm':
        result = number / 10
    else:
        result = number
print(f'{result:.3f}')