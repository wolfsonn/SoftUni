name = input()
counter = 1
marks_sum = 0
fail_counter = 0
is_excluded = False
while counter <= 12:
    mark = float(input())
    if mark >= 4:
        marks_sum += mark
        counter += 1
    else:
        fail_counter += 1
    if fail_counter == 2:
        is_excluded = True
        break
if is_excluded:
    print(f'{name} has been excluded at {counter} grade')
else:
    average_result = marks_sum / 12
    print(f'{name} graduated. Average grade: {average_result:.2f}')
