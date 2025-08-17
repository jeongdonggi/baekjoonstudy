import sys
from collections import deque

input = sys.stdin.readline

def dfs(v):  # 안쪽부터 탐색
    visited = [0] * (n + 1)
    stack = [v]

    while stack:
        node = stack.pop()
        if visited[node] == 0:
            visited[node] = 1
            print(node, end=' ')
            for next in reversed(arr[node]): # 크기가 작은 것 부터 방문
                if visited[next] == 0:
                    stack.append(next)


def bfs(v):  # 처음부분부터 탐색
    visited = [0] * (n + 1)
    queue = deque([v])

    while queue:
        node = queue.popleft()
        if visited[node] == 0:
            visited[node] = 1
            print(node, end= ' ')
            for next in arr[node]:
                if visited[next] == 0:
                    queue.append(next)

n, m, v = map(int, input().split())

arr = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())

    arr[a].append(b)
    arr[b].append(a)

for key in arr.keys(): # 값 sort
    arr[key].sort()

dfs(v)
print()
bfs(v)