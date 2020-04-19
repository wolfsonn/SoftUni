import math
year_type = str(input())  # leap or normal
holidays = int(input())  # not weekends
weekends_at_home = int(input())
games_at_home = weekends_at_home
games_in_sofia = (holidays * 2 / 3) + ((48 - weekends_at_home) * 3 / 4)
total_games = games_at_home + games_in_sofia
if year_type == 'leap':
    print(math.floor(total_games * 1.15))
else:
    print(math.floor(total_games))