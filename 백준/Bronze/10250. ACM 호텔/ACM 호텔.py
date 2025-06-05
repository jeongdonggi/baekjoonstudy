n = int(input())

result = []

for _ in range(n):
    h, w, n = list(map(int, input().split()))

    y = h if n % h == 0 else n % h
    x = n // h if n % h == 0 else 1 + n // h

    result.append(str(y) + str(x).zfill(2))

for r in result:
    print(r)