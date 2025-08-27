from collections import deque

n, m = map(int, input().split())

arr = []

my = [0, 0]
visited = [[-1 for _ in range(m)] for _ in range(n)]

for j in range(n):
    tmp = []
    for key, value in enumerate(list(map(int, input().split()))):
        if value == 2:
            my[0] = j
            my[1] = key
        elif value == 0:
            visited[j][key] = 0
        tmp.append(value)

    arr.append(tmp)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited[my[0]][my[1]] = 0

queue = deque([my])

while queue:
    num = queue.popleft()
    val = visited[num[0]][num[1]]

    for i in range(4):
        nx = dx[i] + num[1] # x
        ny = dy[i] + num[0] # y

        if 0 <= nx < m and 0 <= ny < n:
            if visited[ny][nx] == -1 and arr[ny][nx] == 1:
                visited[ny][nx] = val + 1
                queue.append([ny, nx])

for v in visited:
    print(*v)