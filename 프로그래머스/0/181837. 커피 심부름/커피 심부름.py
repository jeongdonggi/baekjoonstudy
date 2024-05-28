# 아메리카노 4500 라테 5000

def solution(order):
    answer = 0
    for coffee in order:
        if 'americano' in coffee or 'anything' in coffee:
            answer += 4500
        elif 'cafelatte' in coffee:
            answer += 5000
    return answer