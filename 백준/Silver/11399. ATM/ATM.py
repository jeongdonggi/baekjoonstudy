"""
N명의 사람
줄을 서는 순서에 따라서 인출 시간의 합이 달라짐

"""

n = int(input())
t = list(map(int, input().split()))

t.sort(reverse=True)

result = 0

for i in range(n):
    result += t[i]*(i+1)

print(result)