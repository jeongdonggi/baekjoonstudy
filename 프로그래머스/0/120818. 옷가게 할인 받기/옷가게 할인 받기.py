import math

def solution(price):
    answer = price
    if (price // 500000) > 0:
        answer = math.floor(price*0.8)
    elif (price // 300000) > 0:
        answer = math.floor(price*0.9)
    elif (price // 100000) > 0:
        answer = math.floor(price*0.95)
    return answer