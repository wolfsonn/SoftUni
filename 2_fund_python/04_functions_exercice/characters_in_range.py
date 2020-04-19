string_input = input()
string_list_even = [int(i) for i in string_input if int(i) % 2 == 0]
string_list_odd = [int(i) for i in string_input if int(i) % 2 == 1]
print(f'Odd sum = {(sum(string_list_odd))}, Even sum = {(sum(string_list_even))}')
