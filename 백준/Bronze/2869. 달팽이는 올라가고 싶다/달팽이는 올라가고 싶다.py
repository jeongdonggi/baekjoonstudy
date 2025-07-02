import math

a, b, v = map(int, input().split())
answer = 0

day = a - b # 하루에 올라갈 수 있는 경우
# 마지막의 경우 a만 올라가면 끝
final = a

print(math.ceil(((v - a) / day)) + 1)