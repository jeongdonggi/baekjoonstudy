def solution(n):
    answer = 0
    div = n //7
    left = n % 7
    if left > 0:
        answer += 1
    answer += div
    return answer