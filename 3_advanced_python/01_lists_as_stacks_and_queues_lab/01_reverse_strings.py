string_input = [ch for ch in input()]
string_output = []
for _ in range(len(string_input)):
    string_output.append(string_input.pop())
print("".join(string_output))