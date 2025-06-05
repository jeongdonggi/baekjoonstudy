arr = []

while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    arr.append([a,b,c])


for ar in arr:
    a,b,c = sorted(ar)

    if c**2 == a**2 + b**2:
        print("right")
    else:
        print("wrong")