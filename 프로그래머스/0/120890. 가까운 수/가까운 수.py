def solution(array, n):
    answer = 0
    mini = 100
    array = sorted(array)
    
    for num in array:
        if mini > abs(num - n):
            mini = abs(num -n)
            answer = num
    
    return answer