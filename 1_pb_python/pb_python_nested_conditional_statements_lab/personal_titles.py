age = float(input())
gender = str(input())
is_the_person_young = age < 16
is_the_person_male = gender == 'm'
if is_the_person_young:
    if is_the_person_male:
        print('Master')
    else:
        print('Miss')
else:
    if is_the_person_male:
        print('Mr.')
    else:
        print('Ms.')