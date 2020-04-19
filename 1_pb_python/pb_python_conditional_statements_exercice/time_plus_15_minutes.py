initial_hour = int(input())
initial_minutes = int(input())
initial_time = initial_hour * 60 + initial_minutes
result_time = initial_time + 15
result_hour = result_time // 60 % 24
result_minutes = result_time % 60
if result_minutes < 10:
    print(f'{result_hour}:0{result_minutes}')
else:
    print(f'{result_hour}:{result_minutes}')