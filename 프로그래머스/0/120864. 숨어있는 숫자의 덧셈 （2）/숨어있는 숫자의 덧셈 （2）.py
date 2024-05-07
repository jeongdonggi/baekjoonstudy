def solution(my_string):
    answer = 0
    my_string = my_string.lower()
    # 97 - 122
    result = ""
    for s in my_string:
        if 'a' <= s and s <= 'z':
            result += " "
        else:
            result += s
    
    answer = sum(map(int, result.split()))
    
    return answer