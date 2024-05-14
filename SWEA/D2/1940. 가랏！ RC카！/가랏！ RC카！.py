t = int(input())

for test in range(1, t+1):
	n = int(input()) # N
	v = 0
	answer = 0
	for i in range(n):
		a = list(map(int, input().split()))  # 0 : 유지, 1: 가속 2: 감속, 1 or 2면 따로 값이 주어짐
		if a[0] == 0:
			answer += v
		elif a[0] == 1:
			v += a[1]
			answer += v
		elif a[0] == 2:
			v -= a[1]
			if v <= 0:
				v = 0
			answer += v

	print("#{} {}".format(test,answer))