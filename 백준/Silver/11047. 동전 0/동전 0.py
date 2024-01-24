"""
N 종류의 돈으로 K를 만드려고 함 => 최솟값
"""

n, k = map(int, input().split())

result = 0

li = []
for i in range(n):
    m = int(input())
    li.append(m)

li = li[::-1]

for money in li:
    if k < money:
        continue
    else:
        result += k // money
        k = k % money

print(result)