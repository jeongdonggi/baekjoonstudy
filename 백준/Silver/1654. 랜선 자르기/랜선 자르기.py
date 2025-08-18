import sys

input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

# 이분 탐색
left, right = 1, max(arr)
answer = 0

while left <= right:
    mid = (left + right) // 2
    total = sum(a // mid for a in arr)

    if total >= n:  # 짧다
        answer = mid
        left = mid + 1  # 길어짐
    else:  # 길다
        right = mid - 1  # 짧아짐

print(answer)