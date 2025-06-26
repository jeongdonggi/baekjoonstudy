def solution(id_pw, db):
    answer = 'fail'
    for d in db:
        if d[0] == id_pw[0]:
            answer = 'wrong pw'
            if d[1] == id_pw[1]:
                answer = 'login'
        
    return answer