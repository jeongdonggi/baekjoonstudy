n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())
    if a - c > 0:
        print(f"#{i+1} {a-c}")
    elif b - c > 0:
        print(f"#{i+1} {0}")
    else:
        print(f"#{i+1} {-1}")