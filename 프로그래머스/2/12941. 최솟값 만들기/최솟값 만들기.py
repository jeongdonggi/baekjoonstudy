def solution(A,B):
    answer = 0

    a1 = sorted(A)
    b1 = sorted(B)
    
    a2 = a1[::-1]
    b2 = b1[::-1]
    
    re1 = 0
    re2 = 0
    
    for i in range(len(a1)):
        re1 += a1[i]*b2[i]
        re2 += a2[i]*b1[i]
        
    answer = min(re1, re2)
        
    return answer