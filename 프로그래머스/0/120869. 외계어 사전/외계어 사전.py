def solution(spell, dic):
    answer = 2
    cnt = 0
    for d in dic:
        for sp in spell:
            if d.count(sp) == 1:
                cnt += 1
        if cnt == len(spell):
            answer = 1
            break
        else:
            cnt = 0
    
    
        
    return answer