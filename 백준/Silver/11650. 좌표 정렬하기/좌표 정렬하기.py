n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key=lambda x : (x[0], x[1]))

for a in arr:
    print(*a)