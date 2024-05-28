def solution(strArr):
    lst = [0 for _ in range(30)]
    answer = 0
    for str in strArr:
        lst[len(str)-1] += 1

    answer = max(lst)
    return answer