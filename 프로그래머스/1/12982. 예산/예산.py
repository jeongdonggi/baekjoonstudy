def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        n = budget - i
        if n >= 0:
            answer += 1
            budget = n
    return answer