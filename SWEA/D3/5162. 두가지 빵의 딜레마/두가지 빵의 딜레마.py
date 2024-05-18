t = int(input())

for test in range(1, t+1):
    a, b, c = map(int, input().split())
    answer = 0

    nums = sorted([a,b])

    for num in nums:
        answer += (c // num)
        c = c % num

    print("#{} {}".format(test, answer))