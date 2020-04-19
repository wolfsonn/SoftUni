key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials = {}
run = True
while run:
    farm_result = input().lower().split(" ")
    for i in range(0, len(farm_result), 2):
        material = farm_result[i + 1]
        quantity = int(farm_result[i])
        if material in key_materials:
            key_materials[material] += quantity
            if key_materials['shards'] >= 250:
                print("Shadowmourne obtained!")
                key_materials['shards'] -= 250
                run = False
                break
            elif key_materials['fragments'] >= 250:
                print("Valanyr obtained!")
                key_materials['fragments'] -= 250
                run = False
                break
            elif key_materials['motes'] >= 250:
                print("Dragonwrath obtained!")
                key_materials['motes'] -= 250
                run = False
                break
        else:
            if material not in junk_materials:
                junk_materials[material] = 0
            junk_materials[material] += quantity

key_materials_sorted = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
junk_materials_sorted = dict(sorted(junk_materials.items(), key=lambda x: x[0]))
for (material, quantity) in key_materials_sorted.items():
    print(f"{material}: {key_materials[material]}")
for (material, quantity) in junk_materials_sorted.items():
    print(f"{material}: {junk_materials[material]}")
