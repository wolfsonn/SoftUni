exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes
delta = abs(arrival_time - exam_time)
if arrival_time > exam_time:
    print('Late')
    if delta < 60:
        print(f'{delta} minutes after the start')
    else:
        delta_hours = delta // 60
        delta_minutes = delta % 60
        if delta_minutes < 10:
            print(f'{delta_hours}:0{delta_minutes} hours after the start')
        else:
            print(f'{delta_hours}:{delta_minutes} hours after the start')
elif exam_time - 30 <= arrival_time <= exam_time:
    print('On time')
    if delta < 60:
        print(f'{delta} minutes before the start')
    else:
        delta_hours = delta // 60
        delta_minutes = delta % 60
        if delta_minutes < 10:
            print(f'{delta_hours}:0{delta_minutes} hours before the start')
        else:
            print(f'{delta_hours}:{delta_minutes} hours before the start')
else:
    print('Early')
    if delta < 60:
        print(f'{delta} minutes before the start')
    else:
        delta_hours = delta // 60
        delta_minutes = delta % 60
        if delta_minutes < 10:
            print(f'{delta_hours}:0{delta_minutes} hours before the start')
        else:
            print(f'{delta_hours}:{delta_minutes} hours before the start')