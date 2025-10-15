def solution(rank, attendance):
    answer = 0
    hash_map = {}
    m = [10000, 100, 1]
    # 참여못하는 학생들이 있다. - 참여가능 등수 3명
    for key, value in enumerate(attendance):
        if value:
            hash_map[key] = rank[key]
            
    arr = sorted(hash_map.items(), key=lambda x : x[1])
    for i in range(3):
        answer += arr[i][0] * m[i]
    return answer