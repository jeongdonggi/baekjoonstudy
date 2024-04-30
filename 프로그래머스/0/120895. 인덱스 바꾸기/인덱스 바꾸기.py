def solution(my_string, num1, num2):
    answer = ''
    for key,value in enumerate(my_string):
        if key == num1:
            answer += my_string[num2]
        elif key == num2:
            answer += my_string[num1]
        else:
            answer += value
    return answer