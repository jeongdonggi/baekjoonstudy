def solution(seoul):
    answer = ''
    for str in seoul:
        if str == "Kim":
            answer = (f"김서방은 {seoul.index(str)}에 있다")
    return answer