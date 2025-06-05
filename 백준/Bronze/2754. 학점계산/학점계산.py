def plusOrMinus(s1):
    if s1 == '+':
        return 0.3
    elif s1 == '-':
        return -0.3
    else:
        return 0

ss = input()

result = 0

if ss[0] == 'A':
    result += 4
    result += plusOrMinus(ss[1])
elif ss[0] == 'B':
    result += 3
    result += plusOrMinus(ss[1])
elif ss[0] == 'C':
    result += 2
    result += plusOrMinus(ss[1])
elif ss[0] == 'D':
    result += 1
    result += plusOrMinus(ss[1])

print("{:.1f}".format(result))