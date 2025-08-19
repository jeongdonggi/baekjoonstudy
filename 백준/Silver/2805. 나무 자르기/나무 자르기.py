# 이항 연산 문제

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

trees = list(map(int, input().split()))

answer = 0

left, right = 1, max(trees)

while left <= right:
    mid = (left + right) // 2

    total = sum((tree - mid) if tree - mid > 0 else 0 for tree in trees)

    if total >= m:  # 일단 나무 길이는 맞음
        answer = mid
        left = mid + 1  # 더 크게 잡기
    else:
        right = mid - 1  # 더 작게 잡기
        
print(answer)