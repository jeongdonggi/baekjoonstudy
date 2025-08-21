from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().strip())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited[0][0] = 1

queue = deque([(0, 0)])

answer = 0

while queue:
    my, mx = queue.popleft()
    for i in range(4):
        ny = my + dy[i]
        nx = mx + dx[i]

        if 0 <= nx < m and 0 <= ny < n:
            if visited[ny][nx] == 0 and arr[ny][nx] == 1:
                visited[ny][nx] = visited[my][mx] + 1 # 최단거리
                if nx == m-1 and ny == n-1:
                    print(visited[ny][nx])
                    exit(0)

                queue.append((ny, nx))
