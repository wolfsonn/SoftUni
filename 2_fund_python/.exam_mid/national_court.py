employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
total_people_count = int(input())
capacity_per_hour = employee_one + employee_two + employee_three
hours_needed = 0
breaks = 0
while total_people_count > 0:
    total_people_count -= capacity_per_hour
    hours_needed += 1
    breaks += 1
    if breaks % 4 == 0:
        hours_needed += 1

print(f'Time needed: {hours_needed}h.')
