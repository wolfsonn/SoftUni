import math
income = float(input())
grade = float(input())
minimal_wage = float(input())
social_scholarship = minimal_wage * 0.35
excellent_result_scholarship = grade * 25
scholarship = float()
if income >= minimal_wage:
    if grade < 5.5:
        print('You cannot get a scholarship!')
    else:
        scholarship = math.floor(excellent_result_scholarship)
        print(f'You get a scholarship for excellent results {scholarship} BGN')
else:
    if grade <= 4.5:
        print('You cannot get a scholarship!')
    elif grade < 5.5:
        scholarship = math.floor(social_scholarship)
        print(f'You get a Social scholarship {scholarship} BGN')
    else:
        if social_scholarship > excellent_result_scholarship:
            scholarship = math.floor(social_scholarship)
            print(f'You get a Social scholarship {scholarship} BGN')
        else:
            scholarship = math.floor(excellent_result_scholarship)
            print(f'You get a scholarship for excellent results {scholarship} BGN')