def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        result = int(str(num)[s:s+l])
        if result > k:
            answer.append(result)
    
    return answer