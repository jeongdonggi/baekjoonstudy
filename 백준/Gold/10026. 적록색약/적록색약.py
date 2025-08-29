from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n = int(input())

arr = [list(input()) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
visited_rg = [[False] * n for _ in range(n)]

cnt = 0
cnt_rg = 0

# R G 동일 시
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt += 1
            q = deque([(i, j)])  # y, x
            visited[i][j] = True

            while q:
                y, x = q.popleft()

                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]

                    if 0 <= ny < n and 0 <= nx < n:
                        if not visited[ny][nx] and arr[ny][nx] == arr[y][x]:
                            q.append((ny, nx))
                            visited[ny][nx] = True

        if not visited_rg[i][j]:
            cnt_rg += 1
            q = deque([(i, j)])  # y, x
            visited_rg[i][j] = True

            while q:
                y, x = q.popleft()

                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]

                    if 0 <= ny < n and 0 <= nx < n:
                        if not visited_rg[ny][nx]:
                            if arr[y][x] == 'B' and arr[ny][nx] == 'B':
                                q.append((ny, nx))
                                visited_rg[ny][nx] = True
                            elif arr[y][x] != 'B' and arr[ny][nx] != 'B':
                                q.append((ny, nx))
                                visited_rg[ny][nx] = True

print(cnt, cnt_rg)
