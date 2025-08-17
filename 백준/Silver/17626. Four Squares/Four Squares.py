import sys
input = sys.stdin.readline

n = int(input())
cnt = [0, 1, 2, 3]  # 최소값 저장

for i in range(4, n + 1):
    m = []
    for j in range(int(i ** (1/2)), 0, -1):
        m.append(cnt[i - (j ** 2)] + 1)

    cnt.append(min(m))

print(cnt[n])