n = int(input())

stack = []

for _ in range(n):
    s = list(input().split())

    do = s[0]

    if do == 'push':
        stack.append(s[1])
    elif do == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif do == 'size':
        print(len(stack))
    elif do == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif do == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[len(stack)-1])