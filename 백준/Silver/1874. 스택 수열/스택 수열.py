from collections import deque

n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

stack = []
result = []

cnt = 1

for num in arr:

    while num >= cnt:
        stack.append(cnt)
        result.append('+')
        cnt += 1

    if stack.pop() == num:
        result.append('-')
    else:
        print('NO')
        break
else:
    print(*result, sep='\n')