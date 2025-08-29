import heapq

t = int(input())

for _ in range(t):
    k = int(input())
    min_q = []
    max_q = []

    visited = [False] * k

    for i in range(k):
        s, n = input().split()
        n = int(n)

        if s == 'I':
            heapq.heappush(min_q, (n, i))
            heapq.heappush(max_q, (-n, i))
            visited[i] = True # 들어옴
        else:
            if n == 1:
                while max_q and not visited[max_q[0][1]]: # 동기화
                    heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = False # 나감
                    heapq.heappop(max_q)
            else:
                while min_q and not visited[min_q[0][1]]: # 동기화
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = False  # 나감
                    heapq.heappop(min_q)


    # 못 뺀애들 삭제
    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)

    if not min_q or not max_q:
        print('EMPTY')
    else:
        print(-max_q[0][0], min_q[0][0])

