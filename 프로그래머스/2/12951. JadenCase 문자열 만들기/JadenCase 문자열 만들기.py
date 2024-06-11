def solution(s):
    answer = ''
    lst = list(s.split(' '))
    
    for l in lst:
        if len(l) > 0:
            answer += l[0].upper()+l[1:].lower()
        answer += ' '
            
    return answer[:-1]