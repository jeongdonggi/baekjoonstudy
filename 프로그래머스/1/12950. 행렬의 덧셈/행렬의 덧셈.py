def solution(arr1, arr2):
    answer = arr1
    
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            answer[i][j] += arr2[i][j]
    
    return answer