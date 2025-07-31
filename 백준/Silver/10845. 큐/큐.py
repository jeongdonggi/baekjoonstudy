from collections import deque

n = int(input())

queue = deque()

for _ in range(n):
    s = list(input().split())

    do = s[0]

    if do == 'push':
        queue.append(s[1])
    elif do == 'pop':
        print(queue.popleft() if queue else -1)
    elif do == 'size':
        print(len(queue))
    elif do == 'empty':
        print(0 if queue else 1)
    elif do == 'front':
        print(queue[0] if queue else -1)
    elif do == 'back':
        print(queue[-1] if queue else -1)

