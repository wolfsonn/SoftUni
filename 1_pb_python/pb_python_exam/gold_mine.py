location_number = int(input())
for location in range(location_number):
    expected_amount = float(input())
    days_on_location = int(input())
    total_harvest = 0
    for day in range(days_on_location):
        harvested_amount = float(input())
        total_harvest += harvested_amount
    average_harvest_per_day = total_harvest / days_on_location
    if average_harvest_per_day >= expected_amount:
        print(f'Good job! Average gold per day: {average_harvest_per_day:.2f}.')
    else:
        gold_needed = expected_amount - average_harvest_per_day
        print(f'You need {gold_needed:.2f} gold.')
