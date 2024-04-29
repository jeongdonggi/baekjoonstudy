def solution(arr):
    answer = []
    for num in arr:
        n = num
        if num >= 50 and num % 2 == 0:
            n =num/2
        elif num < 50 and num % 2 == 1:
            n = num*2
        answer.append(n)
    return answer