def solution(sides):
    answer = 2
    sides = sorted(sides)
    if sides[2] - (sides[1] + sides[0]) < 0:
        answer = 1
    return answer