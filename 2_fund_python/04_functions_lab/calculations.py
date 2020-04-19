input_operator = input()
number_one = int(input())
number_two = int(input())


def calculate(operator, a, b):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = a / b
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    return result


print(calculate(input_operator, number_one, number_two))