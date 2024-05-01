def solution(n):
    answer = 0
    # 6의 배수를 n으로 나누었을 때 0이 나와야 됨 이때 배수 값을 리턴
    cnt = 1
    while 6*cnt % n != 0:
        cnt += 1
    answer = cnt
    return answer