t = int(input())
answer = ''
for test in range(1, 1 + t):
    if '3' in str(test) or '6' in str(test) or '9' in str(test):
        three = str(test).count('3') + str(test).count('6') + str(test).count('9')
        answer += '-'*three + " "
    else:
        answer += str(test) + " "

print(answer)