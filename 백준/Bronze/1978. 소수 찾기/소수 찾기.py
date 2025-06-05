n = int(input())
arr = list(map(int, input().split()))

count = 0

def func(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False

    return True

for a in arr:
    if func(a):
        count += 1

print(count)