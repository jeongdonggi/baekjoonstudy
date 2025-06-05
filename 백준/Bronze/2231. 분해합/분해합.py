n = int(input())

result = []

for i in range(1, n+1):
    k = 0
    for j in str(i):
        k += int(j)

    if i + k == n:
        result.append(i)

if len(result) != 0:
    print(min(result))
else:
    print(0)