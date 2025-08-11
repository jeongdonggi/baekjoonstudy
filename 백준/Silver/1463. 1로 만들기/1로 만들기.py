import sys
input = sys.stdin.readline

n = int(input())

cache = [0] * (n + 1)

for i in range(2, n + 1):
    cache[i] = cache[i-1] + 1

    if i % 2 == 0:
        cache[i] = min(cache[i], cache[i // 2] + 1)
    if i % 3 == 0:
        cache[i] = min(cache[i], cache[i // 3] + 1)

print(cache[n])


# cache = {1: 0, 2: 1, 3: 1}
#
# def solution(n):
#     if n in cache: # 이미 저장되었다면 return
#         return cache[n]
#
#     two = float('inf')
#     three = float('inf')
#
#     minus = solution(n-1) # -1
#     if n % 2 == 0:
#         two = solution(n//2) # // 2
#     if n % 3 == 0:
#         three = solution(n//3) # // 3
#
#     m = min(minus , two, three) # 이중 가장 작은 값
#     cache[n] = m + 1 # 한 번 수행하였으니 + 1
#     return cache[n] # 값 return
#
# num = int(input())
#
# print(solution(num))