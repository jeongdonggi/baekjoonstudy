## 원래 코드
"""
t= int(input())
#           y,x
# 우 하 좌 상 0,0
x_lst = [1, 0, -1, 0]
y_lst = [0, 1, 0, -1]

for T in range(1, t+1):
	n = int(input())
	lst = [[0 for _ in range(n)] for _ in range(n)] # 이차원 리스트 생성

	answer = ""

	cnt = 0
	x = 0
	y = 0

	for i in range(1,n*n+1): # 이차원 리스트 크기만큼
		lst[y][x] = i

		if x != x+x_lst[cnt % 4] and y == y+y_lst[cnt % 4]: # 끝에 다 다랐을 때 => 얘가 문제
			if x < x+x_lst[cnt % 4] and x == n - 1:
				cnt += 1
			elif x > x+x_lst[cnt % 4] and x == 0:
				cnt += 1
		elif x == x+x_lst[cnt % 4] and y != y+y_lst[cnt % 4]: # 끝에 다 다랐을 때 => 얘가 문제
			if y < y+y_lst[cnt % 4] and y == n - 1:
				cnt += 1
			elif y > y+y_lst[cnt % 4] and y == 0:
				cnt += 1
		if lst[y + y_lst[cnt % 4]][x + x_lst[cnt % 4]] != 0:
			cnt += 1

		x += x_lst[cnt % 4]
		y += y_lst[cnt % 4]

	for j in range(n):
		answer += " ".join(str(x) for x in lst[j]) + '\n'

	print("#{} \n{}".format(T, answer.strip()) )

"""
## GPT가 최적화 해준거임 내가 푼거 아님

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
