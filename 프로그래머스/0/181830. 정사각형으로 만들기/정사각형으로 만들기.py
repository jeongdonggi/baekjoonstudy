def solution(arr):
    col = len(arr)
    row = len(arr[0])
    
    if col > row:
        for i in range(col):
            for j in range(col-row):
                arr[i].append(0)
    elif col < row:
        for i in range(row-col):
            arr.append([0 for _ in range(row)])
                
    return arr