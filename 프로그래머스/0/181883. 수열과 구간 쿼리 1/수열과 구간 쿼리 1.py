def solution(arr, queries):
    answer = []
    for lst in queries:
        for i in range(lst[0],lst[1]+1):
            arr[i] += 1
    
    answer = arr
    return answer