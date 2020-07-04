from collections import deque

bomb_effect = deque([int(x) for x in input().split(', ')])
bomb_casing = [int(x) for x in input().split(', ')]
crafted_datura = 0
crafted_cherry = 0
crafted_smoke = 0
full = False

def which_bomb(materials):
    if materials == 40:
        return 'Datura Bombs'
    elif materials == 60:
        return 'Cherry Bombs'
    elif materials == 120:
        return 'Smoke Decoy Bombs'
    else:
        return 'neither'


while len(bomb_effect) > 0 and len(bomb_casing) > 0 and not full:
    materials = bomb_effect[0] + bomb_casing[-1]
    if which_bomb(materials) != 'neither':
        if which_bomb(materials) == 'Datura Bombs':
            crafted_datura += 1
        elif which_bomb(materials) == 'Cherry Bombs':
            crafted_cherry += 1
        elif which_bomb(materials) == 'Smoke Decoy Bombs':
            crafted_smoke += 1
        if crafted_smoke >= 3 and crafted_cherry >= 3 and crafted_datura >= 3:
            full = True
        bomb_effect.popleft()
        bomb_casing.pop()
    else:
        bomb_casing[-1] -= 5

if full:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if sum(bomb_effect) == 0:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effect])}")
if sum(bomb_casing) == 0:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(x) for x in reversed(bomb_casing)])}")

print(f"Cherry Bombs: {crafted_cherry}")
print(f"Datura Bombs: {crafted_datura}")
print(f"Smoke Decoy Bombs: {crafted_smoke}")