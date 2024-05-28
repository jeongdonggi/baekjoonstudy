import copy
def solution(arr):
    answer = 0
    cnt = 0
    
    while True:
        old = copy.deepcopy(arr)
        for k, a in enumerate(arr):
            if a >= 50 and a % 2 == 0:
                arr[k] = a // 2
            elif a < 50 and a % 2 == 1:
                arr[k] = a * 2 +1
        if old == arr:
            break
        cnt += 1
        
    answer = cnt
    return answer

"""
arr 원소: 50보다 크거나 같고 짝수면 /2
50보다 작고 홀수면 *2+1
이때 arr(x) == arr(x+1)일 때의 x를 구하기


"""