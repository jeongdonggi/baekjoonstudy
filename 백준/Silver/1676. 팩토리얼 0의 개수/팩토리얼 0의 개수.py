n = int(input())

cnt = 0

fact = 1

for i in range(1, n+1):
    fact *= i

for s in reversed(str(fact)):
    if s == '0':
        cnt += 1
    else:
        break

print(cnt)