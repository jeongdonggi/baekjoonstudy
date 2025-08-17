import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]  # 좌우
dy = [-1, 1, 0, 0]  # 상하

# dfs(nx, ny) # 재귀 런타임 에러 나옴
def dfs(x, y):
    visited[y][x] = 1
    stack = [(x, y)]
    
    while stack: # stack을 이용하여 주변 배추 탐색
        sx, sy = stack.pop()
        for d in range(4):
            nx = sx + dx[d]
            ny = sy + dy[d]

            if 0 <= nx < m and 0 <= ny < n:  # 범위 체크
                if arr[ny][nx] == 1 and visited[ny][nx] == 0:  # 옆에 배추있음 따라감
                    visited[ny][nx] = 1
                    stack.append((nx, ny))

t = int(input())

for j in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)] # 밭

    for _ in range(k): # 배추
        x, y = map(int, input().split())
        arr[y][x] = 1

    visited = [[0] * m for _ in range(n)] # 방문

    count = 0 # 접근
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1 and visited[y][x] == 0:  # 새로운 배추
                dfs(x, y)
                count += 1 # 접근 하였습니다

    print(count)