n, k = map(int,input().split())

# n개 # 중에서 k개를 뽑는 경우의 수를 구하는 문제
# n! / (k! * (n-k)!)

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact

print(round(factorial(n)/(factorial(k) * factorial(n-k))))