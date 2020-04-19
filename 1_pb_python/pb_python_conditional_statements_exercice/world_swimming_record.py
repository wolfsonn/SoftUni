world_record = float(input()) # seconds
distance = float(input()) # meters
time_per_meter = float(input()) # seconds
resistance_slowdown = distance // 15 * 12.5 # meters, meters, seconds
player_time = distance * time_per_meter + resistance_slowdown
delta = abs(player_time - world_record)
if player_time < world_record:
    print(f'Yes, he succeeded! The new world record is {player_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {delta:.2f} seconds slower.')