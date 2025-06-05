n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())

result = 0

for a in arr:
    result += (a // t) + (1 if a % t != 0 else 0)

result1 = n // p
result2 = n % p

print(result)
print(result1, result2)