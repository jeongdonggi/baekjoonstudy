n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

result = 0

for j in arr:
    if k < j:
        continue

    result += k // j
    k = k % j

print(result)