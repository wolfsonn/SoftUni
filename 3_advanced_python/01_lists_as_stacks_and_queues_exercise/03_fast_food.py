from collections import deque

food_quantity = int(input())
orders = deque(input().split(' '))

print(max(int(x) for x in orders))
for _ in range(len(orders) + 1):
    if len(orders) == 0:
        print('Orders complete')
        break
    elif food_quantity - int(orders[0]) < 0:
        pass
    elif food_quantity - int(orders[0]) >= 0:
        food_quantity -= int(orders.popleft())
if len(orders) > 0:
    print(f'Orders left: {" ".join(orders)}')