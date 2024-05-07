def solution(i, j, k):
    answer = 0
    for i in range(i,j+1):
        for s in str(i):
            if str(k) in s:
                answer += 1
    return answer