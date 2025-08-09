import sys

input = sys.stdin.readline

n = int(input())

arr = set()

for _ in range(n):
    a = list(input().split())
    action = a[0]
    number = 0
    if len(a) == 2:
        number = int(a[1])
    if action == 'add':
        arr.add(number)
    elif action == 'remove':
        arr.discard(number)
    elif action == 'check':
        print(1 if number in arr else 0)
    elif action == 'toggle':
        if number in arr:
            arr.remove(number)
        else:
            arr.add(number)
    elif action == 'all':
        arr = set(range(1, 21))
    elif action == 'empty':
        arr.clear()