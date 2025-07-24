n = int(input())

# 666만 들어가면 됨
cnt = 0

num = 666
while True:
    if '666' in str(num):
        cnt += 1

    if cnt == n:
        break

    num += 1

print(num)