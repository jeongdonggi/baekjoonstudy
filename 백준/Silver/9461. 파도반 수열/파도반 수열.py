import sys

input = sys.stdin.readline

cache = [0, 1, 1, 1, 2, 2, 3]

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

for i in range(7, max(arr)+1):
    cache.append(cache[i - 1] + cache[i - 5])

for a in arr:
    print(cache[a])
