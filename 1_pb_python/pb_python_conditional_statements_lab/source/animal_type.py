animal = str(input())
animal_type_1 = 'mammal'
animal_type_2 = 'reptile'
animal_type_3 = 'unknown'
if animal == 'dog':
    animal_type = animal_type_1
elif animal == 'crocodile':
    animal_type = animal_type_2
elif animal == 'tortoise':
    animal_type = animal_type_2
elif animal == 'snake':
    animal_type = animal_type_2
else:
    animal_type = animal_type_3
print(animal_type)