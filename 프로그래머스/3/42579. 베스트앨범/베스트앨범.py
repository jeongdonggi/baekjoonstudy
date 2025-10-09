def solution(genres, plays):
    answer = []
    
    hash_map = {}
    
    for i in range(len(genres)):
        
        if genres[i] not in hash_map:
            hash_map[genres[i]] = [[i, plays[i]]]
        else:
            hash_map[genres[i]].append([i, plays[i]])
                
    sort_hash_map = sorted(hash_map.items(), 
                           key=lambda x: sum(value for key, value in x[1])
                           , reverse=True)
                                       
    for key, value in sort_hash_map:
        sort_value = sorted(value, key=lambda x : (-x[1], x[0]))
                                   
        for i in range(min(2, len(sort_value))):
            answer.append(sort_value[i][0])
    
    return answer