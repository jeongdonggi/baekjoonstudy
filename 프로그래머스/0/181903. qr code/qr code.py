def solution(q, r, code):
    answer = ''
    for k, v in enumerate(code):
        if k % q == r:
            answer += v
    return answer