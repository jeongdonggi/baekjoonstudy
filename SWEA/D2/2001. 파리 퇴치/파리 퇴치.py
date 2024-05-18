t = int(input())

for test in range(1, t + 1):
    answer = 0
    n, m = map(int, input().split())
    lst = [list(map(int,input().split())) for _ in range(n)]
    fly_lst = []

    for i in range(n-m+1):
        for j in range(n-m+1):
            fly_dead = 0
            for a in range(m):
                for b in range(m):
                    fly_dead += lst[i+a][j+b]
            fly_lst.append(fly_dead)
    answer = max(fly_lst)
    print("#{} {}".format(test, answer))