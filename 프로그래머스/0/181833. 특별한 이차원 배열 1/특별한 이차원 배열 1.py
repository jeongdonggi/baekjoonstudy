def solution(n):
    answer = []
    for i in range(n):
        answer.append([1  if j == i else 0 for j in range(n)])
    return answer