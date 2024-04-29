def solution(n):
    answer = 0
    answer = sum([x ** 2 for x in range(0,n+1,2)]) if n % 2 == 0 else sum(x for x in range(1,n+1,2))
    return answer