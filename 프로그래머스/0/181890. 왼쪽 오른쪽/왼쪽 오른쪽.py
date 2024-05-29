def solution(str_list):
    answer = []
    
    for k, str in enumerate(str_list):
        if str == 'l':
            return str_list[:k]
        elif str == 'r':
            return str_list[k+1:]

    return answer