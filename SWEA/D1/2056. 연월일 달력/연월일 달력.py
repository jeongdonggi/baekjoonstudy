t = int(input())
check = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for test in range(1, 1 + t):
    n = input()
    y= n[:4]
    m= n[4:6]
    d = n[6:8]

    if int(m) < 1 or int(m) > 12 or check.get(int(m)) < int(d):
        answer = -1
    else:
        answer = "/".join(x for x in [y, m, d])

    print("#{} {}".format(test,answer))
