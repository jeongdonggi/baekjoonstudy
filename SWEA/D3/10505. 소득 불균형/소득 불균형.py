n = int(input())
for i in range(1,n+1):
    num = int(input())
    num_list = list(map(int, input().split()))
    cnt = 0
    avg = sum(num_list) / len(num_list)
    for j in num_list:
        if j <= avg:
            cnt += 1
    print("#{} {}".format(i, cnt))