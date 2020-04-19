divisor = float(input())
bound = float(input())
N = bound
while N > 0:
    if N % divisor != 0:
        N -= 1
    else:
        print(int(N))
        break