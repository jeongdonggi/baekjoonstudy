def solution(sizes):    
    width = 0
    height = 0
    
    for x, y in sizes:
        width = max(width , min(x, y)) # 작은 값들 중에 큰 값
        height = max(height, max(x, y)) # 큰 값들 중에 큰 값
        
    return width * height