yes = 'YES'
no = 'NO'

n = int(input())

for _ in range(n):

    s = input()

    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) <= 0:
                stack.append(i)
                break
            stack.pop()

    if len(stack) == 0:
        print(yes)
    else:
        print(no)