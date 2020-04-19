points = int(input())
if points <= 100:
    bonus_points = 5
elif points <= 1000:
    bonus_points = float(points * 0.20)
else:
    bonus_points = float(points * 0.10)
if points % 2 == 0:
    bonus_points_2 = 1
elif points % 10 == 5:
    bonus_points_2 = 2
else:
    bonus_points_2 = 0
print(bonus_points + bonus_points_2)
print(points + bonus_points + bonus_points_2)