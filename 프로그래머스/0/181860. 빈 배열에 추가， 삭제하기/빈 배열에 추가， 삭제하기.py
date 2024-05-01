def solution(arr, flag):
    answer = []
    for key, value in enumerate(flag):
        if value:
            for j in range(arr[key]*2):
                answer.append(arr[key])
        else:
            for j in range(arr[key]):
                answer.pop()
    return answer