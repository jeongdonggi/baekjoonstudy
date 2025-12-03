from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for dungeon in permutations(dungeons):
        tired = k
        count = 0
        
        for x, y in dungeon:
            if tired >= x:
                tired -= y
                count += 1
        
        answer = max(answer, count)
    
    return answer