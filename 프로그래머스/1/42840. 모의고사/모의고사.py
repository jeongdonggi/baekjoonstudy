def solution(answers):
    
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    answer = []
    
    o = 0
    t = 0
    h = 0
    
    for key, value in enumerate(answers):
        if value == one[key % len(one)]: 
            o += 1
        if value == two[key % len(two)]: 
            t += 1
        if value == three[key % len(three)]: 
            h += 1
            
    if o == max(o,t,h):
        answer.append(1)
    if t == max(o,t,h):
        answer.append(2)
    if h == max(o,t,h):
        answer.append(3)
            
    return answer