def solution(myString):
    answer = ''
    for str in myString:
        if ord(str) < 108:
            answer += "l"
        else:
            answer += str
    return answer