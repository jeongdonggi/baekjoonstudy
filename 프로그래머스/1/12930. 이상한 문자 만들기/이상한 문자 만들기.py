def solution(s):
    answer = ''
    for k in s.split(' '):
        for n, i in enumerate(k):
            if n % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
        answer += ' '
        
    return answer[:len(s)]