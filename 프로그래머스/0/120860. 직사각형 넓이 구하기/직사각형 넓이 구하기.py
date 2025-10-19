def solution(dots):
    answer = 0
    
    x = set()
    y = set()
    
    for nx, ny in dots:
        x.add(nx)
        y.add(ny)
        
    answer = (max(x) - min(x)) * (max(y) - min(y))
    
    return answer