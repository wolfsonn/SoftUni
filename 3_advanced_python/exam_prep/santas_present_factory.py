from collections import deque

materials = [int(x) for x in input().split(' ')]
magic_level = deque([int(x) for x in input().split(' ')])
crafted_toys = []


def which_toy(magic_amount):
    if magic_amount == 150:
        return 'Doll'
    elif magic_amount == 250:
        return 'Wooden train'
    elif magic_amount == 300:
        return 'Teddy bear'
    elif magic_amount == 400:
        return 'Bicycle'
    else:
        return 'neither'


while len(materials) > 0 and len(magic_level) > 0:
    if materials[-1] == 0:
        materials.pop()
        continue
    if magic_level[0] == 0:
        magic_level.popleft()
        continue
    magic = materials[-1] * magic_level[0]
    if which_toy(magic) != 'neither':
        crafted_toys.append(which_toy(magic))
        materials.pop()
        magic_level.popleft()
    elif magic < 0:
        materials.append(materials.pop() + magic_level.popleft())
    elif magic > 0:
        materials[-1] += 15
        magic_level.popleft()
if ('Doll' in crafted_toys and 'Train' in crafted_toys) or ('Teddy bear' in crafted_toys and 'Bicycle' in crafted_toys):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if sum(materials) > 0:
    print(f'Materials left: {", ".join(reversed([str(x) for x in materials]))}')
if sum(magic_level) > 0:
    print(f'Magic left: {", ".join([str(x) for x in magic_level])}')
if 'Bicycle' in crafted_toys:
    print(f'Bicycle: {crafted_toys.count("Bicycle")}')
if 'Doll' in crafted_toys:
    print(f'Doll: {crafted_toys.count("Doll")}')
if 'Teddy bear' in crafted_toys:
    print(f'Teddy bear: {crafted_toys.count("Teddy bear")}')
if 'Wooden train' in crafted_toys:
    print(f'Wooden train: {crafted_toys.count("Wooden train")}')
