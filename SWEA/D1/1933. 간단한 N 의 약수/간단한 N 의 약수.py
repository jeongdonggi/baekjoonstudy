n = int(input())
answer = []

for i in range(1, n//2+1):
    if n % i == 0:
        answer.append(i)

answer.append(n)


print(' '.join(str(x) for x in answer))