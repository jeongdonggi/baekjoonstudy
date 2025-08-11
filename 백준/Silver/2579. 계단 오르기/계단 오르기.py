import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)
stair =[0] + [int(input()) for i in range(n)]

dp[1] = stair[1]
if n > 1:
    dp[2] = stair[2] + stair[1] # 무조건 두개 밟는게 큼

for i in range(3, n + 1):
    dp[i] = stair[i] + max(dp[i-2], dp[i-3] + stair[i-1])
    # 한칸 건너 뛰는 경우와 연속인 경우 구하기

print(dp[n])