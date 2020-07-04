from collections import deque

pumps_count = int(input())
pumps_list = deque()
for _ in range(pumps_count):
    pumps_list.append([int(x) for x in input().split(' ')])
route = 0


def route_check(route):
    fuel = 0
    distance = 0
    good_route = True
    for _ in range(pumps_count):
        fuel += pumps_list[0][0]
        distance += pumps_list[0][1]
        if fuel < distance:
            good_route = False
            break
        else:
            fuel -= distance
    if not good_route:
        pumps_list.append(pumps_list.popleft())
        route += 1
        route_check(route)
    else:
        print(route)


route_check(route)
