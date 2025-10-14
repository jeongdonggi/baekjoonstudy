def solution(keyinput, board):
    answer = []
    d = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0]}
    
    distict_x = (board[0] - 1) // 2
    distict_y = (board[1] - 1) // 2
    
    x = 0
    y = 0
    
    for key in keyinput:
        nx, ny = d[key]
        new_x = x + nx
        new_y = y + ny
        
        if -distict_x <= new_x <= distict_x:
            x = new_x
        if -distict_y <= new_y <= distict_y:
            y = new_y
    
    answer.append(x)
    answer.append(y)
    
    return answer