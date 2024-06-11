def solution(picture, k):
    answer = []
    for pic in picture:
        for i in range(k):
            result = ''
            for p in pic:
                result += p*k
            answer.append(result)
                
    return answer