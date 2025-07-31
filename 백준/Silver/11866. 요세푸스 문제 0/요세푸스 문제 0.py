from collections import deque

n, k = map(int, input().split())
cnt = k

queue = deque(i for i in range(1, n+1))

print('<',end='')
while len(queue) != 1:
    cnt -= 1

    p = queue.popleft()

    if cnt != 0:
        queue.append(p)
    else:
        print(p, end=', ')
        cnt = k

print(queue.pop(), end='>')