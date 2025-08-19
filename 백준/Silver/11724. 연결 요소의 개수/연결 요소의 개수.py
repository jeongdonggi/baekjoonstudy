import sys

input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    stack = [v]

    while stack:
        s = stack.pop()

        for item in arr[s]:
            if visited[item] == 1:
                continue

            visited[item] = 1
            stack.append(item)


n, m = map(int, input().split())

arr = {i: [] for i in range(1, n + 1)}

visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())

    arr[u].append(v)
    arr[v].append(u)

cnt = 0

for i in range(1, n + 1):
    if visited[i] == 1:
        continue

    dfs(i)
    cnt += 1

print(cnt)