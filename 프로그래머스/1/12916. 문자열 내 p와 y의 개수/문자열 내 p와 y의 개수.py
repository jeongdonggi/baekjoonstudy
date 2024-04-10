def solution(s):
    answer = True
    
    s1 = s.lower()
    
    if s1.count('p') != s1.count('y'):
        answer = False

    return answer