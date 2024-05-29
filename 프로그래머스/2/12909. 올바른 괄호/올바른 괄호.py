def solution(s):
    answer = True
    
    stk = []
    
    for i in s:
        if i == '(':
            stk.append(i)
        else:
            if not stk:
                return False
            stk.pop()
    
    if len(stk) > 0:
        return False

    return True