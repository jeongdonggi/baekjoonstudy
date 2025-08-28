from collections import deque

n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = []

visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1:

            queue = deque([(i, j)])
            visited[i][j] = True

            cnt = 1

            while queue:
                num = queue.popleft()

                for k in range(4):
                    nx = dx[k] + num[1]
                    ny = dy[k] + num[0]

                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[ny][nx] == 1 and not visited[ny][nx]:
                            visited[ny][nx] = True
                            queue.append((ny, nx))
                            cnt = cnt + 1

            if cnt != 0:
                result.append(cnt)

print(len(result))
print(*sorted(result), sep='\n')