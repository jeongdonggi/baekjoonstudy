import math

def solution(n):
    print(math.sqrt(n))
    answer = 1 if math.sqrt(n) == int(math.sqrt(n)) else 2
    return answer