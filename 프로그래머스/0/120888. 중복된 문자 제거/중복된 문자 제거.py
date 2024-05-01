def solution(my_string):
    answer = ''
    li = []
    for str in my_string:
        if str in li:
            continue
        else:
            answer += str
            li.append(str)
    
    return answer