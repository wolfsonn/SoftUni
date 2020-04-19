animal = str(input())
animal_type = str()
if animal == 'dog':
    animal_type = 'mammal'
elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    animal_type = 'reptile'
else:
    animal_type = 'unknown'
print(animal_type)