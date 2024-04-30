def solution(order):
    answer = 0
    for s in str(order):
        if s in '369':
            answer += 1
    return answer