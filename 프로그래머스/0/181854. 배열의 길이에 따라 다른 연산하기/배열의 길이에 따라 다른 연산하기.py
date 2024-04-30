def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:
        # 홀수에 넣기
        answer = [x+n if key % 2 != 0 else x for key, x in enumerate(arr) ]
    else:
        answer = [x+n if key % 2 == 0 else x for key, x in enumerate(arr) ]
    return answer