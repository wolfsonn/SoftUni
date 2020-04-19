team_name = str(input())
games_played = int(input())
total_length = 0
games_with_penalties = 0
games_with_overtime = 0
for game in range(games_played):
    game_length = int(input())
    total_length += game_length
    if game_length > 120:
        games_with_penalties += 1
    elif game_length > 90:
        games_with_overtime += 1
average_length = round(total_length / games_played, 2)
print(f'{team_name} has played {total_length} minutes. Average minutes per game: {average_length:.2f}')
print(f'Games with penalties: {games_with_penalties}')
print(f'Games with additional time: {games_with_overtime}')