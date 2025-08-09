import sys
input = sys.stdin.readline

n, m = map(int, input().split())


dict = {}
for i in range(n):
    key = input().strip()

    dict[key] = i + 1
    dict[str(i+1)] = key

for _ in range(m):
    quiz = input().strip()
    print(dict[quiz])
