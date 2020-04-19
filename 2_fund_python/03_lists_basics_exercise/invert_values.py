numbers = str(input())
numbers_list = numbers.split(" ")
negative_list = []
for i in range(len(numbers_list)):
    num = ((int(numbers_list[i])) * -1)
    negative_list.append(num)
print(negative_list)
