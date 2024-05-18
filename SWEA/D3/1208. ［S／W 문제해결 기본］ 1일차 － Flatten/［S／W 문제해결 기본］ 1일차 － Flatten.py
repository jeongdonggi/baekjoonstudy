for test in range(1, 11):
    answer = 0

    n = int(input()) # 덤프 횟수
    lst = list(map(int, input().split()))

    for i in range(n):
        maximum = max(lst)
        minimum = min(lst)

        lst[lst.index(maximum)] -= 1
        lst[lst.index(minimum)] += 1

    answer = max(lst) - min(lst)

    print("#{} {}".format(test, answer))