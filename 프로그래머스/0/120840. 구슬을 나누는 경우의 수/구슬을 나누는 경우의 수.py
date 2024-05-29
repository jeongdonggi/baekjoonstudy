# 재귀함수 쓰면 런타임 에러
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def solution(balls, share):
    answer = 0
    # m개에서 n개를 뽑는 경우 => 조합
    # (n)! / ((n-m)!m!) 일 경우
    answer = factorial(balls)/(factorial(balls-share)*factorial(share))
    
    return answer