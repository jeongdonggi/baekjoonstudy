result = []

while True:
    try:
            s = input()
            result.append(s)
    except EOFError:
        break

print('\n'.join(result))