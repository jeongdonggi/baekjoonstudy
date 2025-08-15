import sys

input = sys.stdin.readline

n, m = map(int, input().split())
n_arr = [0] + list(map(int, input().split()))

s_arr = [0] * (n + 1)

# sum에서 시간초과가 나서 누적합 리스트 생성
for i in range(1, n + 1):
    s_arr[i] = s_arr[i - 1] + n_arr[i]

for _ in range(m):
    start, end = map(int, input().split())

    print(s_arr[end] - s_arr[start - 1])