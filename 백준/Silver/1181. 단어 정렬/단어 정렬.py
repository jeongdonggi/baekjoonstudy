n = int(input())

arr = dict()
for _ in range(n):
    s = input()
    arr[s] = len(s)

value = dict(sorted(arr.items(), key = lambda x : (x[1], x[0])))

for k in value.keys():
    print(k)