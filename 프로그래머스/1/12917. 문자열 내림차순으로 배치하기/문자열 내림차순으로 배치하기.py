def solution(s):
    answer = "".join(x for x in sorted(s)[::-1])
    return answer