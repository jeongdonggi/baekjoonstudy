import heapq

n = int(input())
queue = []
for _ in range(n):
    n = int(input())
    if n != 0:
        heapq.heappush(queue, (abs(n), n))
    else:
        if not queue:
            print(0)
        else:
            print(heapq.heappop(queue)[1])