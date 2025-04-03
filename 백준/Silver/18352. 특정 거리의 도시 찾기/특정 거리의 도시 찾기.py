from collections import deque

b, n, k, x = map(int, input().split())

graph = [[] for _ in range(b + 1)]

for i in range(n):
    a, y = (list(map(int, input().split())))
    graph[a].append(y)


def solution(graph, x, k):
    visited = [-1] * (b + 1)
    result = []

    queue = deque([x])  # 단일 원소가 되기 때문

    visited[x] = 0

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v] + 1
                if visited[i] == k:
                    result.append(i)

    result.sort()

    if len(result) == 0:
        print(-1)
    else:
        for i in result:
            print(i)


solution(graph, x, k)
