n, m = map(int, input().split())

arr = set(input().strip() for _ in range(n))
out = []

for _ in range(m):
    name = input().strip()

    if name in arr: # list 사용 시 O(n), set 사용 시 O(1)
        out.append(name)

out.sort()
print(len(out))
print(*out, sep='\n')