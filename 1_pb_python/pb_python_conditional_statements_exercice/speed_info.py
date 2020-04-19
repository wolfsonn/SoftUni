speed = float(input())
speed_info = str()
if speed <= 10:
    speed_info = 'slow'
elif speed <= 50:
    speed_info = 'average'
elif speed <= 150:
    speed_info = 'fast'
elif speed <= 1000:
    speed_info = 'ultra fast'
else:
    speed_info = 'extremely fast'
print(speed_info)