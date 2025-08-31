n = int(input())
m = int(input())
s = input()  # list()로 변환할 필요 없음

cnt = 0
answer = 0

i = 0
while i < m-2:
    if s[i: i + 3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == n:
            answer += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(answer)