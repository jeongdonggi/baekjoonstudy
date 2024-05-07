def factorial(num):
    if num > 1:
        return num* factorial(num-1)
    else:
        return 1

def solution(n):
    answer = 10
    for i in range(1,11):
        if factorial(i) > n:
            return i-1

    return answer