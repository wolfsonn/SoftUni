e1 = int(input())
e2 = int(input())
e3 = int(input())
all_e = e1 + e2 + e3
total_people = int(input())
hours = 0
break_hours = 0

while total_people > 0:
    hours += 1
    total_people -= all_e
    if hours % 3 == 0 and total_people > 0:
        break_hours += 1

print(f'Time needed: {hours + break_hours}h.')