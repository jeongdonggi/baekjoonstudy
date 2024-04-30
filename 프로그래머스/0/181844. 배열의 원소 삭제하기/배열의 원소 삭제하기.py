def solution(arr, delete_list):
    answer = []
    for a in arr:
        cnt = 0
        for d in delete_list:
            if a == d:
                cnt += 1
        if cnt == 0:
            answer.append(a)
    return answer