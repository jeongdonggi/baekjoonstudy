n, m = map(int, input().split())

def go(num):
    if len(cache) == m: # m개 고르면 출력
        print(*cache)
        return

    for nxt in range(num, n+1):
        cache.append(nxt)
        go(nxt+1)
        cache.pop() # 하나의 리스트를 이용하여 백트래킹 구현

cache = []
go(1)