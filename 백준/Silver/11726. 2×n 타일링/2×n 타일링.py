import sys

input = sys.stdin.readline

n = int(input())

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i

    return f

result = 0
for k in range(n//2 + 1):
    total = n - k
    result += factorial(total) // (factorial(k) * factorial(total-k))

print(result % 10007)