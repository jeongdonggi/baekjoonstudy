for test in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))

    answer = 0

    for i in range(2, n - 2):
        max_height = max(lst[i-2], lst[i-1], lst[i], lst[i+1], lst[i+2])
        if lst[i] == max_height:
            left_diff = lst[i] - max(lst[i-1], lst[i-2])
            right_diff = lst[i] - max(lst[i+1], lst[i+2])
            if left_diff > 0 and right_diff > 0:
                answer += min(left_diff, right_diff)

    print("#{} {}".format(test, answer))
