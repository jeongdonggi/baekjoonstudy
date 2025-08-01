n, m = map(int, input().split())

for i in range(n, m+1):
    if i < 2:
        continue

    s = True

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            s = False
            break

    if s:
        print(i)