name = input()
counter = 1
marks_sum = 0
while counter <= 12:
    mark = float(input())
    if mark >= 4:
        marks_sum += mark
        counter += 1
average_result = marks_sum / 12
print(f'{name} graduated. Average grade: {average_result:.2f}')