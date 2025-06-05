num = int(input())

narr = []
sarr = []

for _ in range(num):
    n, s = input().split()
    narr.append(n)
    sarr.append(s)

result = []

for i in range(num):
    r = ""
    for s in sarr[i]:
        r += s * int(narr[i])

    result.append(r)

print("\n".join(result))