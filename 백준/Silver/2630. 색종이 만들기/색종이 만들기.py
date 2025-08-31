n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

blue = 0
white = 0

stack = [(0, 0, n)]

# 재귀함수말고 DFS

while stack:
    y, x , size = stack.pop()
    same = True
    im = arr[y][x]

    for i in range(y, y + size):
        for j in range(x, x + size):
            if im != arr[i][j]:
                same = False
                break

        if not same:
            break

    if same:
        if im == 1: # blue
            blue += 1
        else:
            white += 1
    else:
        half = size // 2
        stack.append([y, x, half])
        stack.append([y, x + half, half])
        stack.append([y + half, x, half])
        stack.append([y + half, x + half, half])

print(white)
print(blue)