from collections import deque

def solution(numbers, direction):
    answer = deque(numbers)
    if direction == "right":
        tmp = answer.pop()
        answer.appendleft(tmp)
    else:
        tmp = answer.popleft()
        answer.append(tmp)
        
    return list(answer)