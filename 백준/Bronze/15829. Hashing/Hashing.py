r = 31
m = 1234567891

l = int(input())
s = input()

result = 0
power = 1

for i in range(len(s)):
    result = (result + (ord(s[i]) - 96) * power) % m
    power = power * r  # 지수 대신 곱하기 사용

print(result)