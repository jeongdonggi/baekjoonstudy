from collections import deque

n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    arr[a].append(b)
    arr[b].append(a)

result = 1e9
answer = -1

for i in range(1, n+1):

    visited = [-1] * (n + 1)
    visited[i] = 0

    queue = deque([i])

    while queue:
        num = queue.popleft()

        for a in arr[num]:
            if visited[a] != -1:
                continue

            visited[a] = visited[num] + 1
            queue.append(a)

    total = sum(visited[1:])
    if total < result:
        result = total
        answer = i

print(answer)

