def solution(s):
    answer = 0
    lst = list(s.split())
    for key, value in enumerate(lst):
        if value != 'Z':
            answer += int(value)
        else:
            answer -= int(lst[key-1])
    return answer