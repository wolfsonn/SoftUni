input_string = input()
opening = []
for index in range(len(input_string)):
    if input_string[index] == '(':
        opening.append(index)
    elif input_string[index] == ')':
        print(input_string[opening.pop():index + 1])
