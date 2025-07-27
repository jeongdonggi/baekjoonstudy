arr = []

while True:
    s = input()
    if s == '.':
        break
    else:
        arr.append(s)

for a in arr:
    stack = []
    for s in a:
        if s == '[':
            stack.append(s)
        elif s == '(':
            stack.append(s)
        elif s == ']':
            if len(stack) != 0:
                if stack.pop() != '[':
                    stack.append(s)
                    break
            else:
                stack.append(s)
                break
        elif s == ')':
            if len(stack) != 0:
                if stack.pop() != '(':
                    stack.append(s)
                    break
            else:
                stack.append(s)
                break

    if len(stack) == 0:
        print('yes')
    else:
        print('no')