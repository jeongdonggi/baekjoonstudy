from collections import defaultdict

n = int(input())
s = list(map(int, input().split()))

cnt = defaultdict(int) # default 값 0

left = 0
result = 0

for right in range(n):
    cnt[s[right]] += 1  # 오론쪽

    while len(cnt) > 2:
        cnt[s[left]] -= 1
        if cnt[s[left]] == 0:
            del cnt[s[left]]

        left += 1

    result = max(result, right - left + 1)

print(result)