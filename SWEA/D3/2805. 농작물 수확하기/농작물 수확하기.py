T = int(input())

for t in range(1,T+1):
	a = int(input())
	b = [[] for _ in range(a)]
	for i in range(a):
		b[i] = list(map(str, input().split()))

	center = a//2 # 중간 값
	cnt = 1 # 더해야 할 크기 값
	center_in = 0
	answer = 0

	for j in range(a):
		for k in b[j][0][center: center+cnt]:
			answer += int(k)
		if center == 0 :
			center_in = 1

		if center_in == 0:
			center -= 1
			cnt += 2
		else:
			center += 1
			cnt -= 2

	print("#{} {}".format(t, answer))