def solution(A,B):
    answer = 0

    a1 = sorted(A)
    b2 = sorted(B)[::-1]
    
    for i in range(len(a1)):
        answer += a1[i]*b2[i]

        
    return answer