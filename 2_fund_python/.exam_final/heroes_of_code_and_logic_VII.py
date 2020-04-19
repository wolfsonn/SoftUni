number_of_heroes = int(input())
heroes = {}

for _ in range(number_of_heroes):
    hero_info = input().split(" ")
    hero_name = hero_info[0]
    hero_hp = int(hero_info[1])
    if hero_hp > 100:
        hero_hp = 100
    hero_mp = int(hero_info[2])
    if hero_mp > 200:
        hero_mp = 200
    heroes[hero_name] = [hero_hp, hero_mp]

game_on = True

while game_on:
    command = input()

    if command == "End":
        game_on = False
        break
    tokens = command.split(" - ")

    if tokens[0] == "CastSpell":
        hero = tokens[1]
        mp_needed = int(tokens[2])
        spell_name = tokens[3]
        if heroes[hero][1] >= mp_needed:
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero][1] - mp_needed} MP!")
            heroes[hero][1] -= mp_needed
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif tokens[0] == "TakeDamage":
        hero = tokens[1]
        damage = int(tokens[2])
        attacker = tokens[3]
        if heroes[hero][0] > damage:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0] - damage} HP left!")
            heroes[hero][0] -= damage
        else:
            heroes.pop(hero)
            print(f"{hero} has been killed by {attacker}!")

    elif tokens[0] == "Recharge":
        hero = tokens[1]
        amount = int(tokens[2])
        if heroes[hero][1] + amount > 200:
            print(f"{hero} recharged for {200 - heroes[hero][1]} MP!")
            heroes[hero][1] = 200
        else:
            print(f"{hero} recharged for {amount} MP!")
            heroes[hero][1] += amount

    elif tokens[0] == "Heal":
        hero = tokens[1]
        amount = int(tokens[2])
        if heroes[hero][0] + amount > 100:
            print(f"{hero} healed for {100 - heroes[hero][0]} HP!")
            heroes[hero][0] = 100
        else:
            print(f"{hero} healed for {amount} HP!")
            heroes[hero][0] += amount

heroes_sorted = dict(sorted(heroes.items(), key=lambda x: (-int(x[1][0]), x[0])))
for hero in heroes_sorted.keys():
    print(f"{hero}")
    print(f"  HP: {heroes_sorted[hero][0]}")
    print(f"  MP: {heroes_sorted[hero][1]}")