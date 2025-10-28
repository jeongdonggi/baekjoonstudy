from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0 # 초
    truck_weights = deque(truck_weights)

    total_weight = 0
    
    queue = deque([0] * bridge_length)
    while queue:
        answer += 1 # 초 진행
        total_weight -= queue.popleft() # 초만큼 앞으로 나감
        if truck_weights: # 남은 트럭이 있는 경우
            if (total_weight + truck_weights[0]) <= weight:
                w = truck_weights.popleft()
                total_weight += w
                queue.append(w) # 트럭 올라감
            else:
                queue.append(0) # 암것도 안올라감
        
        if not truck_weights and total_weight == 0:
            break # 이미 다 나감
    
    return answer