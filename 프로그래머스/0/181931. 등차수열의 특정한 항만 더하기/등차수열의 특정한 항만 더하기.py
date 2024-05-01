def solution(a, d, included):
    answer = 0
    in_len = len(included)
    
    for i in range(in_len):
        if included[i]:
            answer += a+i*d
    
    return answer