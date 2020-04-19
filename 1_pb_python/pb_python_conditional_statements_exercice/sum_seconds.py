time_racer_1 = int(input())
time_racer_2 = int(input())
time_racer_3 = int(input())
times_sum = time_racer_1 + time_racer_2 + time_racer_3
times_sum_minutes = times_sum // 60
times_sum_seconds = times_sum % 60
if times_sum_seconds < 10:
    times_sum_format = (f'{times_sum_minutes}:0{times_sum_seconds}')
    print(times_sum_format)
else:
    times_sum_format = (f'{times_sum_minutes}:{times_sum_seconds}')
    print(times_sum_format)