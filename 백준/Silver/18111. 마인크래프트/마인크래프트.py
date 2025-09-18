# 코드를 작성해주세요
n,m,b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

minimum = min(map(min, arr))
maximum = max(map(max, arr))

result = []

# 최소부터 최대까지
for num in range(minimum, maximum + 1):
    plus = 0
    minus = 0
    time = 0

    for i in range(n):     # 이중리스트이기 때문에 이중 for문
        for j in range(m):
            if arr[i][j] < num: # 값이 num보다 작을 경우 : delete + 1
                diff = num - arr[i][j]
                plus += diff 
                time += diff # 꺼내기
            elif arr[i][j] > num: # 값이 num보다 클경우 : insert + 1
                diff = arr[i][j] - num
                minus += diff
                time += 2 * diff # 넣기
    
    if  minus - plus + b >= 0:
        result.append((time, num))
    
result.sort(key=lambda x : [x[0], -x[1]])

print(result[0][0], result[0][1])