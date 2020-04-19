number_1 = int(input())
number_2 = int(input())
number_3 = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_and_subtract(a, b, c):
    return subtract((sum_numbers(a, b)), c)


print(add_and_subtract(number_1, number_2, number_3))
