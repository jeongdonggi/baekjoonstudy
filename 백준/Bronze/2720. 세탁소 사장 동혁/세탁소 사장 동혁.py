n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
m = [25, 10, 5, 1]

result = [[0, 0, 0, 0] for _ in range(n)]

for idx,a in enumerate(arr):
    money = a
    for index, value in enumerate(m):
        result[idx][index] += money // value
        money = money % value

for r in result:
    print(' '.join(str(x) for x in r))