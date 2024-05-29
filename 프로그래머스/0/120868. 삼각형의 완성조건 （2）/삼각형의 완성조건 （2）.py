def solution(sides):
    answer = 0
    # 1번 sides의 max가 변일 때
    c = max(sides)
    a = min(sides)
    for b in range(1,c):
        if c < a+b:
            answer += 1
    # 2번 다른 값이 변일 때
    c2 = max(sides)
    while c2 < sum(sides):
        answer += 1
        c2 += 1
    return answer