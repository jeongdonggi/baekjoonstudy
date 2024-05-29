def solution(ineq, eq, n, m):
    answer = 0
    if eq == '=':
        ineq = ineq + eq
    answer = int(eval(str(n)+ineq+str(m)))
    return answer