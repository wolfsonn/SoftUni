length = int(input())
while length < 10 or 500 < length:
    length = int(input('Please enter a value between 10cm and 500cm.'))
width = int(input())
while width < 10 or 300 < width:
    width = int(input('Please enter a value between 10cm and 300cm.'))
height = int(input())
while height < 10 or 200 < height:
    height = int(input('Please enter a value between 10cm and 200cm.'))
percentage_volume_taken = float(input()) * 0.01
while percentage_volume_taken < 0.000 or 100.000 < percentage_volume_taken:
    percentage_volume_taken = float(input('Please enter a value between 0.000 percent and 100.000 percent.'))
aquarium_volume = int(length * width * height)
aquarium_liters = float(aquarium_volume * 0.001)
liters_needed = float(aquarium_liters * (1 - percentage_volume_taken))
print(f'{liters_needed:.3f}')