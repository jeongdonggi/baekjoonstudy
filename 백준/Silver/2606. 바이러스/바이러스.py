import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
m = int(input())

dict = {i : set() for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())

    dict[a].add(b)
    dict[b].add(a)

visited = set()
visited.add(1)
queue = deque([1])

while queue:
    node = queue.popleft()
    for nxt in dict[node]:
        if nxt not in visited:
            visited.add(nxt)
            queue.append(nxt)

print(len(visited) - 1)