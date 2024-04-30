def solution(arr, idx):
    answer = 0
    answer = "".join(str(x) for x in arr[idx:]).find('1')
    if answer != -1:
        answer += idx
    return answer