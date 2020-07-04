from collections import deque

children = deque(input().split(' '))
step = int(input())
current_toss = 0
while len(children) > 1:
    current_toss += 1
    if current_toss % step != 0:
        children.append(children.popleft())
    elif current_toss % step == 0:
        print(f'Removed {children.popleft()}')
print(f'Last is {children[0]}')
