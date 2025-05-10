n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

result = 1

arr.sort(key=lambda x: (x[1], x[0])) # 종료 시간과 시작시간 기준 정렬

finish = arr[0][1]

for a in arr[1:]:
    if a[0] >= finish:
        finish = a[1]
        result += 1

print(result)