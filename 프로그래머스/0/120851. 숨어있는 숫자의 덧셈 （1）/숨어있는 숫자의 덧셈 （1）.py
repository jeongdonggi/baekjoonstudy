def solution(my_string):
    answer = 0
    for s in my_string:
        if ord(s) >= 48 and ord(s) <= 57:
            answer += int(s)
    return answer