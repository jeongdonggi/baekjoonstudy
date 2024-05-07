def solution(s):
    answer = ''
    cnt = sorted(set(s))
    for c in cnt:
        if s.count(c) == 1:
            answer += c
    
    return answer