# 유클리드 호제법 사용
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))