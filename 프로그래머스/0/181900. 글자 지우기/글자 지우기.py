def solution(my_string, indices):
    answer = ''
    str_list = list(my_string)
    indices = sorted(indices)
    for num in indices:
        str_list[num] = ""
    
    answer = "".join(str_list)
    
    return answer