N = int(input())
a = 0

while N >= 0:
    if (N % 5) == 0:
        print(N//5 + a)
        break
    else:
        N = N - 3
        a += 1
        if N == 0:
            print(a)
            break
else:
    print("-1")