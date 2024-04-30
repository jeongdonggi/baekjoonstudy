def solution(my_string):
    answer = []
    # 49 57
    for str in my_string:
        if ord(str) >= 48 and ord(str) <= 57:
            answer.append(int(str))
    return sorted(answer)