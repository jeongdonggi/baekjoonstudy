n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(input()))

result = n * m

for i in range(n - 7):
    for j in range(m - 7): # 첫 시작 위치
        wcnt = 0
        bcnt = 0

        for k in range(i, i+8):
            for l in range(j, j+8):

                if (k + l) % 2 == 0: # k + l 을 이용하여 체스판 모양으로 비교가 가능하다.
                    if arr[k][l] != 'W': # 시작색이 W. W가 나와야 되는데 W가 아닌 경우
                        wcnt += 1
                    else: # 시작색이 B, B가 나와야 되는데 B가 아닌 경우
                        bcnt += 1
                else:
                    if arr[k][l] != 'B': # 시작색이 W. B가 나와야 되는데 B가 아닌 경우
                        wcnt += 1
                    else: # 시작색이 B, W가 나와야 되는데 W가 아닌 경우
                        bcnt += 1
        
        result = min(result, wcnt, bcnt) # 지금까지 cnt 중 가장 작은 값 찾기

print(result) # 결과 출력
