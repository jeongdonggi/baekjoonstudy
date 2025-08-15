import sys
input = sys.stdin.readline

n = int(input())

cache = [0, 1, 3]

for i in range(3, n+1):
    cache.append((cache[i-1] + 2 * cache[i-2]) % 10007)

print(cache[n])

"""
1: 1
12
2: 3
12
21
22
3: 5
12 (첫칸을 채우게 되면 n -1 인 부분을 채우면 됨)
    12 12
    21
    22

21 12 (첫 칸을 채우게 되면 n-2 인 부분을 채우면 됨)

22 12 (첫 칸을 채우게 되면 n-2 인 부분을 채우면 됨)

-> (n-1) + 2*(n-2) 의 점화식 생성
"""