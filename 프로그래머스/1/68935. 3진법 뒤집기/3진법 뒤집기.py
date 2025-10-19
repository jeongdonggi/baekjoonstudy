def solution(n):
    answer = 0
    s = ''
    # 3진법 만들기
    while n > 0:
        s += str(n % 3) # 반대로 넣기
        n //= 3
        
    for key, value in enumerate(s[::-1]):
        answer += int(value) * (3 ** key)
        
    
    return answer