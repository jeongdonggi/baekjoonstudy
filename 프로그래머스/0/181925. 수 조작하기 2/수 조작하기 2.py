def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        minus = numLog[i+1] - numLog[i]
        if minus == 1:
            answer += 'w'
        elif minus == -1:
            answer += 's'
        elif minus == 10:
            answer += 'd'
        elif minus == -10:
            answer += 'a'
            
        
    return answer