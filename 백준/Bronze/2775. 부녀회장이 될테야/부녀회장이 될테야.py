# 아래층 자신 호수까지 1부터 더하기

t = int(input())
k = []
n = []
for i in range(t):
    k.append(int(input()))
    n.append(int(input()))

result = []

for i in range(t):
    arr = [[i for i in range(1, n[i]+1)]]  # 0부터 시작

    for level in range(1, k[i] + 1):  # 0층이 있으므로 1부터 시작
        tmp = []
        for room in range(n[i]):
            tmp.append(sum(arr[level - 1][:room+1]))

        arr.append(tmp)

    result.append(arr[k[i]][n[i]-1])

print('\n'.join(map(str, result)))
