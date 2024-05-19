t = int(input())
for test in range(1, 1 + t):
    answer = []
    n = int(input())
    lst = [[0 for _ in range(n)] for _ in range(n)]
    """
    0
    0 1
    0 1 => 0+1 2
    0 1 => 0+ 1 2 => 1+2 4
    """
    for i in range(n):
        for j in range(i+1):
            if i <= 1 or j == 0 or j == i:
                lst[i][j] = 1
            else:
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]

    print("#{}".format(test))
    for i in range(n):
        s = ""
        for x in lst[i]:
            if x != 0:
                s += str(x) + " "
        print(s.strip())
