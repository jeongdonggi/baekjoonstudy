def solution(myString):
    answer = sorted([str for str in myString.split('x') if str != '' ])
    return answer