import sys
input = sys.stdin.readline

# 다이나믹
cache = {0: (1,0), 1: (0,1)}

def fibonacci(n):
    if n in cache:
        return cache[n]
    else:
        zero1, one1 = fibonacci(n-1)
        zero2, one2 = fibonacci(n-2)
        cache[n] = (zero1 + zero2, one1 + one2)
        return cache[n]

n = int(input().strip())

for _ in range(n):
    m = int(input().strip())
    zero, one = fibonacci(m)
    print(zero, one)