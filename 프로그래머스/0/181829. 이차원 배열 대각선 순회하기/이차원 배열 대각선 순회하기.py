def solution(board, k):
    answer = 0
    bor_len1 = len(board) # 4
    bor_len2 = len(board[0]) # 3

    for i in range(k+1):
        if i < bor_len1:
            for j in range(k+1-i):
                if j < bor_len2:
                    answer += board[i][j]
            
    
    return answer