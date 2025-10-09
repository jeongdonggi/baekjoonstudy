from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    
    while queue:
        if queue[0][1] == max(queue, key=lambda x: x[1])[1]:
            key, value = queue.popleft()
            answer += 1
            if key == location:
                return answer
        else:
            queue.append(queue.popleft())
    
    return answer