def solution(array):
    answer = 0
    
    array = sorted(array)
    le = len(array)
    
    answer = array[le//2]
    
    return answer