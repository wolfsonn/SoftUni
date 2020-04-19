team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_A_players = len(team_A)
team_B_players = len(team_B)
terminated = False
cards = input()
cards_list = cards.split()
if cards != "0":
    for i in range(len(cards_list)):
        penalty_list = (cards_list[i]).split("-")
        if "A" in penalty_list:
            player = int(penalty_list[1])
            if player in team_A:
                team_A.remove(int(player))
                team_A_players -= 1
                if team_A_players < 7:
                    terminated = True
                    break
        else:
            player = int(penalty_list[1])
            if player in team_B:
                team_B.remove(int(player))
                team_B_players -= 1
                if team_B_players < 7:
                    terminated = True
                    break
print(f'Team A - {team_A_players}; Team B - {team_B_players}')
if terminated:
    print('Game was terminated')
