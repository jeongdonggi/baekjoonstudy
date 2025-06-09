n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0

l = len(arr)

for i in range(l):
    for j in range(i + 1, l):
        for k in range(j + 1, l):
            total = arr[i] + arr[j] + arr[k]
            if result < total <= m:
                result = total

print(result)