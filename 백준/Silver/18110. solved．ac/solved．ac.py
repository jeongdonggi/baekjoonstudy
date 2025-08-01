n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

if n == 0:
    print(0)
else:
    m = n * 0.15

    m = int(m) + 1 if m - int(m) >= 0.5 else int(m)

    arr.sort()
    ar = arr[m: n - m]

    r = sum(ar)/ len(ar)

    print(int(r) + 1 if r - int(r) >= 0.5 else int(r))