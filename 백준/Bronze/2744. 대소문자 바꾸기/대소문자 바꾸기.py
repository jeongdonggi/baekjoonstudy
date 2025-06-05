ss = input()

result = []

for s in ss:
    if s.isupper():
        result.append(s.lower())
    else:
        result.append(s.upper())

print(''.join(result))