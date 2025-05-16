arr = []

for i in range(28):
    arr.append(int(input()))

arr.sort()
result = []

for j in range(1, 28):
    if arr[j] - arr[j-1] != 1:
        result.append(arr[j] -1)

if len(result) == 0:
    result.append(1)
    result.append(30)

if len(result) == 1:
    result.append(30)

print(result[0])
print(result[1])