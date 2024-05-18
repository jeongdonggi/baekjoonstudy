t = int(input())

for test in range(1, t + 1):
    answer = 0
    n, a, b = map(int, input().split())

    # n 명이 최소 일 때
    # n 명이 최대일 때
    # 둘 다 아니오라고 대답을 했을 수 있구나
    # 최솟값이 n보다 작고 a+b-최솟값이 n보다 작거나 같아야 됨 => 최대
    # a + b -n이 => 최소

    maximum = min(a,b)
    minimum = (a+b)-n if (a+b)-n >= 0 else 0

    answer = " ".join(str(x) for x in [maximum,minimum])

    print("#{} {}".format(test, answer))