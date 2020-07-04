clothes = [int(x) for x in input().split(' ')]
values_sum = 0
rack_capacity = int(input())
racks = 0
if rack_capacity == 0 or sum(clothes) == 0:
    print(racks)
else:
    while len(clothes) > 0:
        if clothes[-1] == 0:
            clothes.pop()
        elif values_sum + clothes[-1] >= rack_capacity:
            racks += 1
            values_sum = 0
        elif values_sum + clothes[-1] < rack_capacity:
            values_sum += clothes.pop()
    print(racks + 1)
