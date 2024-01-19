m = int(input())
sum = 0

n = 1000 - m

num = [500, 100, 50, 10, 5, 1]

for i in num:
    if(n >= i):
        sum += (n//i)
        n = n % i

print(sum)