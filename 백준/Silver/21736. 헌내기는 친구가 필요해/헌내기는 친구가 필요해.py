from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())

arr = []
me = [0, 0]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    al = list(input())

    for key, value in enumerate(al):
        if value == 'I':
            me[0] = i
            me[1] = key
        if value == 'X':
            visited[i][key] = True

    arr.append(al)

# O 빈공간, X 벽, I 도연, P 사람

answer = 0

def bfs(y, x):
    answer = 0

    queue = deque([(y, x)])
    visited[y][x] = True

    while queue:
        my, mx = queue.popleft()
        for i in range(4):
            nx = mx + dx[i]
            ny = my + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    if arr[ny][nx] == 'P':
                        answer += 1

    print(answer if answer > 0 else 'TT')

bfs(me[0], me[1])