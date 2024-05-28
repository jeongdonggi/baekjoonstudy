def solution(n):
    answer = []
    cnt = 2
    while n > 1:
        if n % cnt == 0:
            answer.append(cnt)
            n //= cnt
        else:
            cnt += 1
    
    return sorted(list(set(answer)))