def solution(absolutes, signs):
    answer = 123456789
    answer = sum(num if signs[key] else num*-1 for key,num in enumerate(absolutes))
    return answer