def solution(n, m):
    answer = []
    a = n
    b = m
    mi = 1
    ma = 1
    # 최대 최소 찾기
    for i in range(min(n,m)+1,1,-1):
        if a % i == 0 and b % i == 0:
            mi = i
            break
    
    ma = n * m // mi
    
    answer.append(mi)
    answer.append(ma)
    return answer