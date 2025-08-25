from collections import deque

n, k = map(int, input().split())

MAX = 100000

visited = [-1 for _ in range(MAX + 1)]

queue = deque([n])
visited[n] = 0

while queue:
    num = queue.popleft()

    if num == k:
        print(visited[k])
        break

    for nxt in (num -1, num + 1, num * 2):
        if 0 <= nxt < MAX + 1 and visited[nxt] == -1:
            visited[nxt] = visited[num] + 1
            queue.append(nxt)