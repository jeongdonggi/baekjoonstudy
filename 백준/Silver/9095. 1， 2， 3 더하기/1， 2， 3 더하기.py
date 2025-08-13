import sys

input = sys.stdin.readline

# dp는 점화식으로 플기

T = int(input())

cache = [0] * 12
cache[1] = 1
cache[2] = 2
cache[3] = 4

for i in range(4, 12):
    cache[i] = cache[i-1] + cache[i-2] + cache[i-3]

for _ in range(T):
    n = int(input())
    print(cache[n])
