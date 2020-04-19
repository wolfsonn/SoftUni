daily_goal = int(input())
command = str()
details = str()
daily_total = 0
while daily_total < daily_goal and command != 'closed':
    command = str(input())
    if command == 'closed':
        money_needed = daily_goal - daily_total
        print(f'Target not reached! You need {money_needed}lv. more.')
        break
    else:
        details = str(input())
        if command == 'haircut':
            if details == 'mens':
                daily_total += 15
            elif details == 'ladies':
                daily_total += 20
            else:
                daily_total += 10
        else:
            if details == 'touch up':
                daily_total += 20
            else:
                daily_total += 30
if daily_total >= daily_goal:
    print(f'You have reached your target for the day!')
print(f'Earned money: {daily_total}lv.')