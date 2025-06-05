n = int(input())

arr = []

for _ in range(n):
    arr.append(input())

result = []

for a in arr:
    result.append("".join([a[0] + a[-1]]))

print("\n".join(result))