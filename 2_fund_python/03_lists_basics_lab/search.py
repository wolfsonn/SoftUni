n = int(input())
word = input()
list = []
redacted_list = []
for i in range(n):
    list.append(input())
print(list)
for i in range(n-1, -1, -1):
    element = list[i]
    if word not in element:
        list.remove(element)
print(list)