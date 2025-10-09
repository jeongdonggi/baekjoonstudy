import math

def solution(progresses, speeds):
    answer = []
    
    arr = []
    
    for key, progress in enumerate(progresses):
        num = math.ceil((100 - progress) / speeds[key])
        arr.append(num)
        
    tmp = arr[0]
    cnt = 1
    for i in range(1, len(arr)):
        if tmp < arr[i]:
            tmp = arr[i]
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
    
    answer.append(cnt)
    
    return answer