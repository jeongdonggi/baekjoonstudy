def solution(arr):
    answer = []
    lst = []
    for key, value in enumerate(arr):
        if value == 2:
            lst.append(key)
    if len(lst) == 0:
        answer.append(-1)
    else:
        answer = arr[lst[0]:lst[-1]+1]
    
    return answer