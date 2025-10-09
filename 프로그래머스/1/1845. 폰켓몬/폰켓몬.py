def solution(nums):
    answer = 0
    
    n = len(nums) // 2
    
    set_nums_n = len(set(nums))
    
    if set_nums_n >= n:
        answer = n
    else:
        answer = set_nums_n
    
    return answer