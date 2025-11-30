def solution(brown, yellow):
    answer = []
    
    for n in range(1,int(yellow ** (1/2))+1):
        height = n
        if yellow % n != 0:
            continue
        width = yellow // n
        
        if brown == ((width + 1) + (height + 1)) * 2:
            answer.append(width + 2)
            answer.append(height + 2)
            break
        
    return answer