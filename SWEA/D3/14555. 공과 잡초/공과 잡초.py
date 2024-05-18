t = int(input())

for test in range(1, t+1):
    s = list(input())
    lst = []

    answer = 0
    cnt = 0
    for str in s:
        if str == '(' or str == ')':
            if cnt == 0 and str == ')':
                lst.pop()
                answer += 1
            else:
                lst.append(str)
                cnt = 0
        else:
            cnt += 1
    answer += len(lst)
    print("#{} {}".format(test,answer))