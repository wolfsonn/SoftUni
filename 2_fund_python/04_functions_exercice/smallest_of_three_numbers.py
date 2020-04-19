input_number_one = int(input())
input_number_two = int(input())
input_number_three = int(input())


def smallest_of_three(a, b, c):
    l = [a, b, c]
    return sorted(l)[0]


print(smallest_of_three(input_number_one, input_number_two, input_number_three))