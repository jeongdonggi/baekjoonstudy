t = int(input())

for test in range(1, t + 1):
    answer = ""

    n, m = map(int, input().split())

    one = 0
    two = 0

    for i in range(m,-1,-1):
        if 2*i + m-i == n:
            one = m-i
            two = i
            break


    answer = " ".join(str(x) for x in [one, two])

    print("#{} {}".format(test, answer))