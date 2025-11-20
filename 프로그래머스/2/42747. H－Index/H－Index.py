def solution(citations):
    answer = 0

    citations.sort(reverse=True)
    
    for key, value in enumerate(citations):
        if value >= key + 1: # 역순으로 보면 하나씩 돌렸을 떄 확인이 가능
            answer += 1
            
    return answer