def solution(s):
    answer = []
    cnt = 0
    zero_cnt = 0
    while len(s) != 1:
        zero_cnt += s.count('0')
        x = s.replace('0','')
        c = len(x)
        s = bin(c)[2:]
        cnt += 1
    answer.append(cnt)
    answer.append(zero_cnt)
    return answer