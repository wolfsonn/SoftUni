def line(index, n):
    indent = " " * (n - index - 1)
    stars = "* " * index + "*"
    return f'{indent}{stars}'


def print_rhombus(n):
    for i in range(n):
        print(line(i, n))

    for i in range(n - 2, -1, -1):
        print(line(i, n))


print_rhombus(int(input()))
