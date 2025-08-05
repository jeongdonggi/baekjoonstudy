def Round(n):
    if n >= 0:
        return int(n + 0.5)
    else:
        return int(n - 0.5)

n = int(input()) # 홀수

num = []

for _ in range(n):
    num.append(int(input()))

print(Round(sum(num) / n)) # 산술평균
num2 = sorted(num) 
print(num2[n//2]) # 중앙값

s = set(num2)

sarr = {i: 0 for i in s}  # 딕셔너리로 변경

for j in num2:
    sarr[j] += 1
# 최빈값
sarr_sort = sorted(sarr.items(), key=lambda x: [-x[1], x[0]])
if len(sarr_sort) > 1 and sarr_sort[0][1] == sarr_sort[1][1]:
    print(sarr_sort[1][0])
else:
    print(sarr_sort[0][0])
print(num2[-1] - num2[0]) # 범위