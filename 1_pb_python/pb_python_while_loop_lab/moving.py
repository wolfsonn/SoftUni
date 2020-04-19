width = int(input())
length = int(input())
height = int(input())
number_of_boxes = input()  # boxes volume; number or 'Done'
total_boxes = int(number_of_boxes)
apartment_volume = width * length * height
while total_boxes <= apartment_volume and number_of_boxes != 'Done':
    number_of_boxes = input()
    if number_of_boxes == 'Done':
        break
    else:
        total_boxes += int(number_of_boxes)
        if apartment_volume < total_boxes:
            break
volume_delta = abs(apartment_volume - total_boxes)
if number_of_boxes == 'Done' and apartment_volume > total_boxes:
    print(f'{volume_delta} Cubic meters left.')
else:
    print(f'No more free space! You need {volume_delta} Cubic meters more.')