def solution(dot):
    answer = 0
    # 양양 1 양음 4 음양 2 음음 3
    if dot[0]* dot[1] > 0: # 양양 or 음음
        if dot[0] < 0:
            answer = 3
        else:
            answer = 1
    else: # 양음 or 음양
        if dot[0] < 0:
            answer = 2
        else:
            answer = 4
        
    return answer