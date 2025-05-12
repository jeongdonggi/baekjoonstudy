s = int(input())
n = 1
result = 0

while True:
    if s < n:
        break

    s -= n
    result += 1
    n += 1  # n하나씩 올리기

print(result)