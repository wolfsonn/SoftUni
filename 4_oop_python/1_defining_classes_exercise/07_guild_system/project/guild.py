from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.player_list = []

    def assign_player(self, player: Player):
        if player.guild == 'Unaffiliated':
            player.guild = self.name
            self.player_list.append(player)
            return f'Welcome player {player.name} to the guild {self.name}'
        elif player.guild == self.name:
            return f'Player {player.name} is already in the guild.'
        else:
            return f'Player {player.name} is in another guild.'

    def kick_player(self, player: str):
        if player not in self.player_list:
            return f'Player {player} is not in the guild.'
        else:
            player.guild = 'Unaffiliated'
            self.player_list.remove(player)
            return f'Player {player} has been removed from the guild.'

    def guild_info(self):
        result = f'Guild: {self.name}\n'
        for p in self.player_list:
            result += f'{p.player_info()}\n'
        return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
