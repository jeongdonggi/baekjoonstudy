n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

result = [1 for _ in range(n) ]

for key, value in enumerate(arr):
    for a in arr:
        if value[0] < a[0] and value[1] < a[1]:
            result[key] += 1

for r in result:
    print(r, end=' ')