int_input = str(input())
amount = int(input())
int_list = int_input.split()
int_list_num = []
for i in int_list:
    int_list_num.append(int(i))
sorted_list = int_list_num.copy()
sorted_list.sort()
smallest_nums = sorted_list[:amount]
for i in smallest_nums:
    if i in int_list_num:
        int_list_num.remove(i)
print(int_list_num)