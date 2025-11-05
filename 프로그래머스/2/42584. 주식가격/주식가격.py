def solution(prices):
    answer = [0] * len(prices)
    
    stack = []
        
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            point = stack.pop()
            answer[point] = i - point
            
        stack.append(i)
        
    while stack:
        point = stack.pop()
        answer[point] = len(prices) - (point + 1)
        
    return answer