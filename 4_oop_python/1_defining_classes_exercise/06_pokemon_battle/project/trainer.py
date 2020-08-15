from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.pokemon_details() not in self.pokemon:
            self.pokemon.append(pokemon.pokemon_details())
            return f'Caught {pokemon.name} with health {pokemon.health}'
        else:
            return f'This pokemon is already caught'

    def release_pokemon(self, pokemon_name: str):
        for p in self.pokemon:
            if pokemon_name in p:
                self.pokemon.remove(p)
                return f'You have released {pokemon_name}'
            else:
                return 'Pokemon is not caught'

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n'
        for p in self.pokemon:
            result += f'- {p}'
        return result


trainer = Trainer("Stamat")
pokemon = Pokemon("Pesho", 90)
trainer.add_pokemon(pokemon)
print(trainer.trainer_data())
