def solution(n):
    answer = 0
    for i in range(3, n+1): # 약수 구하기
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                answer += 1
                break
    return answer