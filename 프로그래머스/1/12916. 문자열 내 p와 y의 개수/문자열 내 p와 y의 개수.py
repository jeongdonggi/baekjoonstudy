def solution(s):
    answer = True
    
    s = s.lower()
    
    intP = 0
    intY = 0
    
    for word in s:
        if word == 'p':
            intP += 1
        elif word == 'y':
            intY += 1
    
    if intP != intY:
        answer = False

    return answer