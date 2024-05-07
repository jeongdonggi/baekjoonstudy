def solution(emergency):
    answer = []
    diction = {}
    for key ,num in enumerate(sorted(emergency,reverse=True)):
        diction[num] = key+1
    for num in emergency:
        answer.append(diction.get(num))
    return answer