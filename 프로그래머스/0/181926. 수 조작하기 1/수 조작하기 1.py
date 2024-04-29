def solution(n, control):
    answer = n
    chr = ['w','s','d','a']
    num = [1,-1,10,-10]
    for col in control:
        for key, value in enumerate(chr):
            if col == value:
                answer += num[key]
    return answer