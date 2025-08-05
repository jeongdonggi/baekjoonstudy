from collections import deque

num = int(input())
for _ in range(num):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    queue = deque([(i, p) for i, p in enumerate(priority)])

    cnt = 0

    while queue:
        if queue[0][1] == max(queue, key=lambda x: x[1])[1]:
            idx, value = queue.popleft()
            cnt += 1
            if idx == m:
                print(cnt)
                break
        else:
            queue.append(queue.popleft())