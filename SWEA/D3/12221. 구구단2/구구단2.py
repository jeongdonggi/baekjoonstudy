n = int(input())
for i in range(1,n+1):
    a, b = map(int,input().split())
    answer = -1
    if a < 10 and b < 10:
        answer = a * b
    print("#{} {}".format(i,answer))