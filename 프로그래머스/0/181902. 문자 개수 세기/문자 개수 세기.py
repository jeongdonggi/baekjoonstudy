def solution(my_string):
    answer = [0 for _ in range(52)]
    for st in my_string:
        if st.isupper():
            answer[ord(st)-65] += 1
        else:
            answer[ord(st)-97+26] += 1

    return answer