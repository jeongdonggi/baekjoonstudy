def solution(arr):
    answer = arr
    n = 0
    # 2의 배수보다 작을 때
    while True:
        if len(arr) <= 2**n:
            break
        n += 1
    
    for i in range(2**n-len(arr)):
        answer.append(0)
    
    return answer