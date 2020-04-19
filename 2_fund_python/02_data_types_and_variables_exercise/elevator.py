persons = int(input())
capacity = int(input())
from math import ceil
courses = ceil(persons / capacity)
print(courses)