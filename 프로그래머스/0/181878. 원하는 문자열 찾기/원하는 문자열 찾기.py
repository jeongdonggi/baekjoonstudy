def solution(myString, pat):
    answer = 0
    
    answer =  1 if pat.lower() in myString.lower() else 0
    
    return answer