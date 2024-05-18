t = int(input())
# 방향: 우, 하, 좌, 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for T in range(1, t + 1):
    n = int(input())
    lst = [[0 for _ in range(n)] for _ in range(n)]  # 이차원 리스트 생성

    x, y = 0, 0
    direction = 0  # 현재 방향: 0은 우, 1은 하, 2는 좌, 3은 상

    for i in range(1, n * n + 1):
        lst[y][x] = i
        nx, ny = x + dx[direction], y + dy[direction]

        # 배열의 경계를 벗어나거나 이미 숫자가 채워진 경우 방향 전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n or lst[ny][nx] != 0:
            direction = (direction + 1) % 4
            nx, ny = x + dx[direction], y + dy[direction]

        x, y = nx, ny

    # 출력 포맷에 맞게 문자열 생성
    answer = ""
    for row in lst:
        answer += " ".join(map(str, row)) + "\n"

    print("#{} \n{}".format(T, answer.strip()))
