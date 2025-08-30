n = int(input())  # 2 * n + 1 번 I O # 0의 갯수?
m = int(input())
s = list(input().strip())

cnt = 0

for i in range(len(s) - (2*n)):
    if s[i] == 'I':
        go = True
        for j in range(2*n):
            if s[i+j] == s[i+j+1]:
                go = False
                break

        if go:
           cnt += 1

print(cnt)