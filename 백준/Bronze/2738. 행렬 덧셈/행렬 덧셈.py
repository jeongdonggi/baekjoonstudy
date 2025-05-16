n, m = map(int, input().split())

a = []
b = []

result = []

for _ in range(n):
    a.append(list(map(int, input().split())))

for _ in range(n):
    b.append(list(map(int, input().split())))

for i in range(n):
    r = []
    for j in range(m):
        r.append((a[i][j] + b[i][j]))
    result.append(r)

for re in result:
    print(" ".join(str(r) for r in re))