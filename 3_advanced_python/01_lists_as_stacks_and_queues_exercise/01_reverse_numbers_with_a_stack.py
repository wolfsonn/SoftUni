numbers_queue = input().split(' ')
new_queue = []
for _ in range(len(numbers_queue)):
    new_queue.append(numbers_queue.pop())
print(' '.join(new_queue))