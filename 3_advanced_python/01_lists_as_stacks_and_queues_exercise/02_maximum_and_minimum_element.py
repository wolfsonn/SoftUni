stack = []
queries_number = int(input())
for _ in range(queries_number):
    queries = input().split(' ')
    if len(queries) == 2:
        stack.append(int(queries[1]))
    elif queries[0] == '2' and len(stack) > 0:
        stack.pop()
    elif queries[0] == '3' and len(stack) > 0:
        print(max(stack))
    elif queries[0] == '4' and len(stack) > 0:
        print(min(stack))
print(', '.join([str(x) for x in stack[::-1]]))