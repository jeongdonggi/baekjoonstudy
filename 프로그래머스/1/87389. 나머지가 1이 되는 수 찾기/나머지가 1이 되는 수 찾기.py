def solution(n):
    n = n - 1
    answer = n
    
    for i in range(2, n//2+1):
        if n % i == 0:
            answer = i
            break
    return answer