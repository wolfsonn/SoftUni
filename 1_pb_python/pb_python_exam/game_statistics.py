minutes = int(input())
player_name = str(input())
if minutes == 0:
    print('Match has just began! ')
elif minutes < 45:
    print('First half time.')
    if 1 <= minutes <= 10:
        print(f'{player_name} missed a penalty.')
        if minutes % 2 == 0:
            print(f'{player_name} was injured after the penalty.')
    elif 10 < minutes <= 35:
        print(f'{player_name} received yellow card.')
        if minutes % 2 == 1:
            print(f'{player_name} got another yellow card.')
    else:
        print(f'{player_name} SCORED A GOAL !!!')
else:
    print('Second half time.')
    if 45 < minutes <= 55:
        print(f'{player_name} got a freekick.')
        if minutes % 2 == 0:
            print(f'{player_name} missed the freekick.')
    elif 55 < minutes <= 80:
        print(f'{player_name} missed a shot from corner.')
        if minutes % 2 == 1:
            print(f'{player_name} has been changed with another player.')
    elif 80 < minutes <= 90:
        print(f'{player_name} SCORED A GOAL FROM PENALTY !!!')
