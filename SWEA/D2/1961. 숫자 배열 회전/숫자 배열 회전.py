t = int(input())

for test in range(1, t+1):
	n = int(input())
	lst = [[] for _ in range(n)]
	for i in range(n):
		lst[i] = list(input().split())
	answer = [[] for _ in range(n)]

	# 90 도 180 도 270 도
	# 90 => 0,2 -> 0,0 180 => 2,2 -> 2,0 270 => 2,0 -> 2,2

	for i in range(n):
		s = []
		fir = ""
		sec = ""
		thr = ""
		for j in range(n):
			fir += lst[n-1-j][i] # 90 => [i][2-j]
			sec += lst[n-1-i][n-1-j] # 180 => [2-j][i]
			thr += lst[j][n-1-i] # 270 => [2-i][2-j]
		answer[i].append(fir + " " + sec + " " + thr)

	print("#{}".format(test))
	for i in range(n):
		print(*answer[i])