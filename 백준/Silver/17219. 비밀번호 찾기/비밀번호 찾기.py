import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

dict = {}

for _ in range(n):
    uri, pw = input().strip().split()

    dict[uri] = pw

for _ in range(m):
    uri = input().strip()
    print(dict[uri])