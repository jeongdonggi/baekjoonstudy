def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        result = []
        for key,n in enumerate(arr):
            if s <= key and key <= e and k < n:
                result.append(n)
        answer.append(min(result) if len(result) > 0 else -1)
    return answer