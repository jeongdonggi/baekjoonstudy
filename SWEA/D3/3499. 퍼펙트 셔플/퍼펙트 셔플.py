t = int(input())

for test in range(1, t + 1):
    answer = []
    n = int(input())
    lst = list(input().split())

    case = n // 2 if n % 2 == 0 else n // 2 + 1

    for i in range(n // 2):
        answer.append(lst[i])
        answer.append(lst[i+case])

    if n % 2 == 1:
        answer.append(lst[n // 2])
        
    answer = " ".join(str(x) for x in answer)

    print("#{} {}".format(test, answer))