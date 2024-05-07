def solution(myStr):
    answer = []
    for i in ['a','b','c']:
        myStr = myStr.replace(i, " ")

    if myStr.strip() != "":
        answer = myStr.split()
    else:
        answer.append("EMPTY")
    
    return answer