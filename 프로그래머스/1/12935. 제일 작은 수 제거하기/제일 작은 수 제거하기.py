def solution(arr):
    point = arr.index(min(arr))
    if len(arr) == 1:
        return [-1]

    answer = arr[:point]+arr[point+1:]

    return answer