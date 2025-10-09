def solution(clothes):
    answer = 1
    
    hash_dict = {}
    
    for cloth in clothes:
        hash_dict[cloth[1]] = hash_dict.get(cloth[1], 1) + 1
        
    for key, value in hash_dict.items():
        answer *= value
    
    return answer - 1